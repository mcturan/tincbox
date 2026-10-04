#!/usr/bin/env python3
"""
TincBox Agent Daemon (tincbox-agent)
Autonomous hardware telemetry, thermal regulation, zero-config pairing,
and WireGuard tunnel watchdog for TincBox hardware appliances.
"""

import os
import sys
import time
import json
import socket
import logging
import subprocess
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [TincBoxAgent] %(levelname)s: %(message)s"
)
logger = logging.getLogger("tincbox-agent")

CONFIG_PATH = Path("/etc/tincbox/config.json")
STATE_PATH = Path("/var/run/tincbox/state.json")

def get_system_telemetry():
    """Gathers local hardware metrics without external dependencies."""
    telemetry = {
        "timestamp": int(time.time()),
        "hostname": socket.gethostname(),
        "cpu": {"cores": os.cpu_count() or 4, "load_1m": 0.0, "temp_c": 0.0},
        "memory": {"total_mb": 0, "used_mb": 0, "free_mb": 0},
        "storage": {"total_gb": 0, "used_gb": 0, "free_gb": 0},
        "tunnel": {"active": False, "peer_ip": None, "handshake_age": None},
        "status": "operational"
    }

    # Load average
    try:
        load = os.getloadavg()
        telemetry["cpu"]["load_1m"] = round(load[0], 2)
    except Exception:
        pass

    # CPU Temperature
    try:
        thermal_zones = list(Path("/sys/class/thermal").glob("thermal_zone*"))
        for zone in thermal_zones:
            temp_file = zone / "temp"
            if temp_file.exists():
                temp_raw = int(temp_file.read_text().strip())
                telemetry["cpu"]["temp_c"] = round(temp_raw / 1000.0, 1)
                break
    except Exception:
        pass

    # Memory Info from /proc/meminfo
    try:
        meminfo = Path("/proc/meminfo").read_text()
        data = {}
        for line in meminfo.splitlines():
            parts = line.split(":")
            if len(parts) == 2:
                key = parts[0].strip()
                val = int(parts[1].split()[0])
                data[key] = val
        total_kb = data.get("MemTotal", 0)
        avail_kb = data.get("MemAvailable", 0)
        telemetry["memory"]["total_mb"] = total_kb // 1024
        telemetry["memory"]["used_mb"] = (total_kb - avail_kb) // 1024
        telemetry["memory"]["free_mb"] = avail_kb // 1024
    except Exception:
        pass

    # Disk Space (Root or /var/lib/tinc)
    try:
        stat = os.statvfs("/var" if Path("/var").exists() else "/")
        total_b = stat.f_blocks * stat.f_frsize
        free_b = stat.f_bavail * stat.f_frsize
        used_b = total_b - free_b
        telemetry["storage"]["total_gb"] = round(total_b / (1024**3), 1)
        telemetry["storage"]["used_gb"] = round(used_b / (1024**3), 1)
        telemetry["storage"]["free_gb"] = round(free_b / (1024**3), 1)
    except Exception:
        pass

    # WireGuard status
    try:
        wg_out = subprocess.check_output(["wg", "show", "wg0", "latest-handshakes"], text=True, stderr=subprocess.DEVNULL)
        if wg_out.strip():
            telemetry["tunnel"]["active"] = True
    except Exception:
        telemetry["tunnel"]["active"] = False

    return telemetry

class LocalPairingHandler(BaseHTTPRequestHandler):
    """Local REST server answering on http://tincbox.local:8088/"""

    def do_GET(self):
        if self.path == "/api/status" or self.path == "/":
            data = get_system_telemetry()
            body = json.dumps(data, indent=2).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif self.path == "/api/ping":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"pong")
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/api/pair":
            # Handshake pairing with TincID
            length = int(self.headers.get("Content-Length", 0))
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            logger.info("Received pairing request from sovereign TincID: %s", payload.get("tinc_id"))
            
            resp = {
                "ok": True,
                "box_id": socket.gethostname(),
                "paired_at": int(time.time()),
                "tunnel_domain": f"{payload.get('tinc_id', 'user')}.tinc.box"
            }
            body = json.dumps(resp).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

def main():
    logger.info("Starting TincBox Hardware Agent Daemon...")
    server = HTTPServer(("0.0.0.0", 8088), LocalPairingHandler)
    logger.info("Local pairing & telemetry service listening on port 8088 (mDNS: tincbox.local:8088)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info("Shutting down agent.")
        server.server_close()

if __name__ == "__main__":
    main()
