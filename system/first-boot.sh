#!/usr/bin/env bash
# TincBox Appliance First Boot Provisioning Script
set -e

echo "=== TincBox Appliance Initial Setup ==="

# 1. Generate local appliance identity
BOX_ID="tincbox-$(cat /dev/urandom | tr -dc 'a-z0-9' | fold -w 6 | head -n 1)"
echo "Setting Appliance Hostname: ${BOX_ID}"
hostnamectl set-hostname "${BOX_ID}"

# 2. Setup mDNS avahi-daemon broadcast
mkdir -p /etc/avahi/services
cat <<EOF > /etc/avahi/services/tincbox.service
<?xml version="1.0" standalone='no'?>
<!DOCTYPE service-group SYSTEM "avahi-service.dtd">
<service-group>
  <name replace-wildcards="yes">${BOX_ID}</name>
  <service>
    <type>_http._tcp</type>
    <port>8088</port>
    <txt-record>model=TincBox-Solo</txt-record>
    <txt-record>version=1.0.0</txt-record>
  </service>
</service-group>
EOF

systemctl restart avahi-daemon || true

# 3. Generate WireGuard Keys if not present
mkdir -p /etc/wireguard
if [ ! -f /etc/wireguard/box_private.key ]; then
    wg genkey | tee /etc/wireguard/box_private.key | wg pubkey > /etc/wireguard/box_public.key
    chmod 600 /etc/wireguard/box_private.key
    echo "WireGuard cryptographic keypair generated."
fi

# 4. Enable and start TincBox Agent Daemon
systemctl daemon-reload
systemctl enable --now tincbox-agent.service || true

echo "=== TincBox Ready: Available at http://tincbox.local:8088 ==="
