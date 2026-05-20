<div align="center">

# 🛡️ DDoS Shield

### *Real-time Network Attack Detection System*

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-red.svg)](https://streamlit.io/)
[![Scapy](https://img.shields.io/badge/Scapy-2.4.5+-green.svg)](https://scapy.net/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20|%20Linux%20|%20macOS-lightgrey)]()

**Detect DDoS attacks in real-time | Get instant email alerts | Monitor network traffic**

[Features](#features) • [Quick Start](#quick-start) • [Installation](#installation) • [Dashboard](#dashboard) • [Email Setup](#email-alerts-setup) • [FAQ](#faq)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Email Alerts Setup](#email-alerts-setup)
- [Dashboard Guide](#dashboard-guide)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Security Recommendations](#security-recommendations)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📖 Overview

**DDoS Shield** is a powerful, real-time DDoS (Distributed Denial of Service) attack detection system that captures live network traffic, identifies abnormal patterns using configurable thresholds, and sends instant email alerts when attacks are detected. The system features a beautiful, cyberpunk-style dashboard for visualizing attack metrics and exporting data for further analysis.

### Why DDoS Shield?

- 🚀 **Real-time detection** - Instant attack identification
- 📧 **Email notifications** - Get alerts immediately
- 📊 **Beautiful dashboard** - Visualize attack patterns
- 💾 **CSV export** - Save data for analysis
- 🔧 **Easy to configure** - Adjust thresholds easily
- 💰 **100% Free** - Open source and free to use

---

## ✨ Features

### Core Features
| Feature | Description |
|---------|-------------|
| 🔍 **Real-time Packet Capture** | Captures live network traffic using Scapy library |
| 🎯 **Automated DDoS Detection** | Identifies potential attacks based on configurable thresholds |
| 📧 **Email Notifications** | Instant email alerts with attack details and recommendations |
| 📊 **Live Dashboard** | Beautiful cyberpunk-style dashboard with real-time updates |
| 📥 **CSV Export** | Export all alert data for further analysis |
| 📈 **Attack Statistics** | Visual charts and metrics for attack patterns |
| 🔄 **Auto-refresh** | Dashboard automatically updates with new alerts |
| 💻 **Cross-platform** | Works on Windows, Linux, and macOS |

### Detection Capabilities
- Threshold-based detection (default: 5 requests/10 seconds)
- Time-window analysis for accurate detection
- IP-based attack tracking
- Severity classification (HIGH/LOW)
- Email cooldown to prevent spam

---

## 🏗️ System Architecture
┌─────────────────────────────────────────────────────────────┐
│ DDoS SHIELD SYSTEM │
└─────────────────────────────────────────────────────────────┘
│
┌─────────────────────┼─────────────────────┐
│ │ │
▼ ▼ ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│ capture │────▶│ logs │────▶│ detector │
│ .py │ │ .json │ │ .py │
│ │ │ │ │ │
│ • Sniff packets│ │ • Store logs │ │ • Analyze │
│ • Extract IPs │ │ • Timestamp │ │ • Check threshold│
│ • Save to JSON│ │ • Protocol │ │ • Generate alerts│
└───────────────┘ └───────────────┘ └───────────────┘
│ │
▼ ▼
┌───────────────┐ ┌───────────────┐
│ alerts │ │ email │
│ .json │ │ alerts │
│ │ │ │
│ • Attack IPs │ │ • Send to │
│ • Counts │ │ Gmail │
│ • Severity │ │ • HTML format │
└───────────────┘ └───────────────┘
│
▼
┌───────────────┐
│ dashboard │
│ .py │
│ │
│ • Live view │
│ • Charts │
│ • CSV export │
└───────────────┘

---

## 📦 Prerequisites

### System Requirements
- **Operating System:** Windows 10/11, Linux (Ubuntu 18.04+), macOS 10.15+
- **Python Version:** 3.7 or higher
- **RAM:** Minimum 2GB (4GB recommended)
- **Storage:** 500MB free space
- **Network:** Administrator/root privileges for packet capture
- **Internet:** Required for email alerts

## 📋 Installation Guide

### Step 1: Install Python

Download and install Python from https://python.org

Verify installation:
```bash
python --version



