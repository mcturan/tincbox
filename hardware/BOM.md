# 📋 TincBox Bill of Materials (BOM) & Reference Hardware Guide

This document outlines the tested reference components for building and mass-producing the three TincBox hardware variants.

---

## 1. TincBox Solo (Reference Platform: N100-ITX / Mini-PC)

| Category | Component Description | Recommended Model / Vendor | Est. Cost (USD) |
|---|---|---|---|
| **SoC / CPU** | Intel Alder Lake-N N100 (4C/4T, 6W TDP) | Integrated BGA SoC | ~$65 (SoC) |
| **Motherboard** | Nano-ITX or Custom Carrier (110x110mm) | Topton / CWWK N100 Industrial SBC | ~$80 |
| **RAM** | 16GB DDR5 4800MHz SO-DIMM (Non-ECC) | Crucial / Samsung DDR5 | ~$42 |
| **Storage** | 1TB M.2 2280 NVMe PCIe 3.0x4 SSD | Samsung 980 / WD Black SN770 | ~$68 |
| **Network** | Dual 2.5GbE LAN (Intel i226-V) | Integrated on SBC | Included |
| **Wireless** | Wi-Fi 6 (AX201 / AX210) + Bluetooth 5.2 | Intel M.2 Key-E Module | ~$18 |
| **Enclosure** | Extruded 6063 Aluminum Fanless Heatsink Case | Custom Tinc Anodized Extrusion | ~$35 |
| **Power Supply** | 12V / 3A USB-C PD 3.0 Wall Adapter | GaN 36W Type-C Adapter | ~$14 |
| **Indicators** | Addressable WS2812B RGB Status LED Ring | Custom 12-LED Halo Diffuser | ~$3 |
| **Total BOM (Solo)** | | | **~$325** |

---

## 2. TincBox Pro (Reference Platform: Core i3-N305 / Dual RAID)

| Category | Component Description | Recommended Model / Vendor | Est. Cost (USD) |
|---|---|---|---|
| **SoC / CPU** | Intel Core i3-N305 (8C/8T, up to 3.8GHz, 15W TDP) | Integrated BGA SoC | ~$120 (SoC) |
| **Motherboard** | Mini-ITX (170x170mm) Dual M.2 + SATA | Industrial Dual M.2 Embedded Board | ~$135 |
| **RAM** | 32GB DDR5 4800MHz SO-DIMM | Kingston / Micron Industrial | ~$85 |
| **Storage (Primary)** | 1TB M.2 2280 NVMe SSD (PCIe 3.0) | Samsung 980 Pro (RAID-1 Drive A) | ~$75 |
| **Storage (Mirror)** | 1TB M.2 2280 NVMe SSD (PCIe 3.0) | Samsung 980 Pro (RAID-1 Drive B) | ~$75 |
| **Expansion Bay** | 1x 2.5" SATA SSD Bay (Toolless Caddy) | Internal SATA Data + Power | ~$8 |
| **Security** | Hardware TPM 2.0 Module | Infineon SLB 9670 / Nuvoton | ~$12 |
| **Enclosure** | Dual-Bay Passive Heatpipe Aluminum Case | Custom Tinc Commercial Enclosure | ~$60 |
| **Power Supply** | 19V / 4.74A (90W) DC Power Brick | FSP / Mean Well Industrial | ~$25 |
| **Total BOM (Pro)** | | | **~$595** |

---

## 3. TincBox Tactical (Reference Platform: CM4 + LoRa + APRS TNC)

| Category | Component Description | Recommended Model / Vendor | Est. Cost (USD) |
|---|---|---|---|
| **Core Compute** | Raspberry Pi Compute Module 4 (CM4104032 - 4GB, 32GB eMMC, Wi-Fi) | Raspberry Pi Foundation | ~$65 |
| **Baseboard** | Custom Ruggedized Carrier with M.2 & SMA headers | Custom Tinc Tactical Baseboard | ~$70 |
| **LoRa Transceiver** | Dual SX1262 LoRa Concentrator (868/915 MHz, +22dBm) | Waveshare / HopeRF Semtech Module | ~$35 |
| **APRS / VHF TNC** | Hardware AX.25 Modulator/Demodulator + VHF Transceiver | Dorji DRA818V (134-174 MHz, 1W) | ~$22 |
| **GPS / GNSS** | u-blox NEO-M9N GNSS Receiver + Active Patch Antenna | u-blox M9N with PPS Sync | ~$28 |
| **Storage** | 512GB M.2 2242 NVMe SSD | Transcend Industrial NVMe | ~$45 |
| **Power System** | Wide Input 9V-36V DC-DC Step-Down with Transient Suppression | TI LM5164 Industrial Regulator | ~$18 |
| **Battery Backup** | Internal LiFePO4 3.2V 6000mAh Buffer Battery | EVE Energy / Custom Pack | ~$24 |
| **Enclosure** | CNC Milled 6061-T6 Aluminum IP67 Rugged Case | O-Ring Sealed Anodized Chassis | ~$85 |
| **Total BOM (Tactical)** | | | **~$392** |
