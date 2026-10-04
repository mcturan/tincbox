# 📦 TincBox — Sovereign Personal Cloud & Hardware Server Appliance

[![Status](https://img.shields.io/badge/Status-Active%20Development-blue.svg)](https://box.tinc.one)
[![License](https://img.shields.io/badge/License-MIT-emerald.svg)](LICENSE)
[![Ecosystem](https://img.shields.io/badge/Ecosystem-Tinc%20One-purple.svg)](https://tinc.one)
[![Portal](https://img.shields.io/badge/Portal-box.tinc.one-orange.svg)](https://box.tinc.one)

> **"Your Data Never Leaves Your Roof."**  
> TincBox is a plug-and-play, sovereign hardware appliance designed to host your private digital universe—notes, inventory, point-of-sale, decentralized identity, and emergency RF mesh communications—with zero external cloud dependence.

---

## 🌟 Vision & Architecture

Modern cloud services compromise your digital sovereignty through subscription paywalls, data harvesting, and centralized outages. **TincBox** bridges the gap between consumer ease-of-use and true local-first computational sovereignty.

```
                    ┌────────────────────────────────────────┐
                    │               TincOne                  │
                    │        (https://tinc.one)              │
                    └───────────────────▲────────────────────┘
                                        │ (TincID Sovereign SSO)
                                        │
           ┌────────────────────────────┴───────────────────────────┐
           │                                                        │
┌──────────▼──────────────┐                              ┌──────────▼──────────────┐
│     TincBox Solo        │                              │     TincBox Tactical     │
│   (Home & Studio)       │                              │  (Off-Grid RF / LoRa)   │
│  - Intel N100 Fanless   │                              │  - CM4 / Dual SX1262    │
│  - 16GB DDR5 + 1TB NVMe │                              │  - APRS AX.25 TNC 144MHz│
│  - Whisper Quiet (<8W)  │                              │  - IP67 CNC Milled Al   │
└──────────▲──────────────┘                              └──────────▲──────────────┘
           │                                                        │
           │◄─────────────────── TincTunnel ────────────────────────►│
           │          (Zero-Config Outbound WireGuard)              │
           │                                                        │
┌──────────▼──────────────┐                              ┌──────────▼──────────────┐
│  Local Client Devices   │                              │  TincPos Local Engine   │
│  (Mobile, Laptop, TV)   │                              │  (Cashier & Terminals)  │
└─────────────────────────┘                              └─────────────────────────┘
```

---

## 🚀 Hardware Editions

### 1. 🏠 TincBox Solo (Home & Creative Studio)
*Built for individuals, families, and creators who demand total data privacy without fan noise.*
- **Processor:** Intel® Alder Lake-N N100 (4 Cores / 4 Threads, up to 3.4 GHz, 6W TDP).
- **Cooling:** Completely Fanless, passive heat-pipe aluminum block casing (0 dB noise).
- **RAM:** 8GB / 16GB DDR5 4800MHz SO-DIMM.
- **Storage:** 512GB / 1TB / 2TB M.2 NVMe PCIe Gen3 (Hardware LUKS2 XTS-AES-256 encrypted).
- **Connectivity:** Dual Intel i226-V 2.5GbE Ethernet, Wi-Fi 6 (802.11ax), Bluetooth 5.2.
- **Power:** 12V USB-C Power Delivery (Idle: ~5.8W, Full Load: ~14W).
- **Dimensions:** 115 × 115 × 42 mm.

### 2. 🏢 TincBox Pro (Commerce & Multi-Branch Enterprise)
*Engineered for bakeries, restaurants, multi-tenant POS networks, and local AI agent execution.*
- **Processor:** Intel® Core™ i3-N305 (8 Cores / 8 Threads, up to 3.8 GHz, 15W TDP) or AMD Ryzen™ Embedded R2000.
- **RAM:** 16GB / 32GB DDR5 (ECC Support).
- **Storage:** Dual M.2 NVMe slots (Configurable Hardware/Software RAID-1 Mirroring) + 1x 2.5" SATA SSD expansion bay.
- **Connectivity:** Dual 2.5GbE LAN with automatic link aggregation & failover bridging.
- **Expansion:** 4x USB 3.2 Gen2, Dual HDMI 2.0 (Dual 4K POS displays), RS232 COM header for legacy fiscal scales/scanners.
- **Power:** Dual redundant 12-19V DC inputs with battery-backup UPS integration.

### 3. 📡 TincBox Tactical (Off-Grid, Disaster Comms & Maritime)
*Designed for amateur radio operators, search and rescue, disaster recovery, and remote expedition vehicles.*
- **Core Engine:** Raspberry Pi Compute Module 4 (CM4) or Rockchip RK3588 with hardware cryptographic accelerator.
- **RF Subsystems:**
  - Dual **Semtech SX1262** LoRa transceivers (868 MHz / 915 MHz Long-Range Mesh, +22 dBm).
  - Integrated **VHF AX.25 TNC** (144.800 MHz APRS beacon & packet messenger).
  - High-precision GNSS/GPS module with PPS sync for accurate telemetry.
- **Enclosure:** CNC-machined 6061-T6 Aircraft Grade Anodized Aluminum with IP67 weatherproof gaskets and external SMA antenna ports.
- **Power Range:** 9V - 36V Wide Input DC (Direct 12V/24V solar panels, vehicle alternator, or LiFePO4 battery pack).

---

## ⚡ Zero-Config "TincTunnel" Networking

Setting up a home server traditionally requires public static IPs, opening router firewall ports, and configuring dynamic DNS. **TincBox eliminates all of this:**

1. **Local Access:**
   - Plug into any home or office router.
   - Instantly resolvable on your local LAN via mDNS: `http://tincbox.local` or `https://tincbox.lan`.
2. **Global Remote Access (TincTunnel):**
   - Outbound-only WireGuard tunnel connects to high-performance sovereign Tinc relay nodes.
   - Penetrates strict ISP CGNAT, mobile LTE/5G firewalls, and hotel Wi-Fi.
   - Your device gets an end-to-end encrypted sovereign hostname: `https://[your-tincid].tinc.box`.
3. **Instant Mobile Pairing:**
   - On first boot, TincBox illuminates an emerald status ring and displays a high-entropy one-time setup QR code.
   - Scan with the **TincID Authenticator** or visit `box.tinc.one/pair`.
   - Cryptographic public keys are exchanged; your device is secured and bound in 10 seconds.

---

## 🛡️ Software Stack: TincOS

TincBox runs **TincOS**, a security-hardened, immutable Linux distribution built for 24/7 reliability:

- **Immutable Read-Only Root:** Core OS files are mounted read-only (`squashfs/erofs`), preventing malware or configuration corruption.
- **Atomic A/B Updates:** System updates install to an alternate partition. If an update fails health checks, it automatically falls back without downtime.
- **Pre-Integrated Microservices:**
  - **TincHub Core Daemon:** Telemetry, process health watchdog, temperature monitor.
  - **TincNote Private Vault:** Local-first zero-knowledge note and file sync.
  - **TincPOS Engine:** Offline-first checkout, order queues, and receipt spooling.
  - **TincSync Engine:** Encrypted peer-to-peer data distribution between boxes.
  - **TincRadio/APRS-IS Daemon:** Background RF telemetry and amateur mesh packet bridge.
- **Encrypted Local Storage:** All user databases are encrypted using LUKS2 keys derived from the on-board TPM 2.0 and your sovereign TincID passphrase.

---

## 🛠️ Directory Structure

```
├── README.md               # Complete architecture, hardware specs, and guide
├── LICENSE                 # Open-Source MIT License
├── hardware/
│   ├── BOM.md              # Detailed Bill of Materials for Solo, Pro, and Tactical
│   └── CHASSIS.md          # Thermal dissipation and mechanical design specs
├── system/
│   ├── tincbox-agent.py    # Local hardware health, telemetry, and pairing daemon
│   ├── first-boot.sh       # Initial setup, WireGuard keygen, and mDNS announcer
│   └── systemd/
│       └── tincbox-agent.service
└── docs/
    ├── PAIRING_PROTOCOL.md # Cryptographic handshake specification
    └── TINCOS_SPEC.md      # Immutable OS partition and update design
```

---

## 📦 Getting Started & Pre-Orders

To learn more, explore interactive 3D mockups, join the waitlist, or pre-order a developer kit:
👉 Visit: **[https://box.tinc.one](https://box.tinc.one)**

---

## 📄 License
This repository and hardware specifications are licensed under the **MIT License**.
Designed with ❤️ by the Tinc Ecosystem Team.
