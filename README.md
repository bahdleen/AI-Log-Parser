# 🧠 AI-Powered Brute Force Login Detection

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Security](https://img.shields.io/badge/Security-Intrusion%20Detection-critical)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-EVE--NG%20%7C%20Linux-lightgrey)

## 🔍 Overview

This Python script is designed to detect **brute force login attempts** by analyzing system logs (e.g., SSH, web login, Windows Event logs) and sending them to an **AI model** (e.g., LLaMA3 hosted via REST API) for threat assessment.

It’s perfect for use in cybersecurity labs, home labs (EVE-NG, GNS3), or lightweight SOC automation environments.

---

## 💡 Features

- ✅ Detects multiple failed login attempts from the same IP
- 🕒 Analyzes time intervals between attempts
- 🌍 Flags suspicious IP behavior
- 🤖 Sends parsed logs to an AI model via API
- 🛡️ Receives mitigation suggestions

---

## ⚙️ Requirements

- Python 3.8+
- `requests` (for API calls)
- System with access to log files (e.g., `/var/log/auth.log`)

Install dependencies:

```bash
pip install requests
