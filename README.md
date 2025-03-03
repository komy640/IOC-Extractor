# IOC Extractor

## Overview
**IOC Extractor** is a powerful Python tool designed to parse large files and extract critical **Indicators of Compromise (IOCs)** for cybersecurity analysis. This tool identifies and extracts various artifacts, including:

- **IP Addresses**
- **Email Addresses**
- **URLs**
- **Executable Files** (EXE, BAT, BIN, SH, PS1, SCR, CMD)
- **Windows Registry Keys**
- **MD5, SHA-1, and SHA-256 Hashes**

This tool aids security analysts, incident responders, and threat hunters in rapid IOC extraction for threat intelligence and forensic analysis.

---

## Features
✅ Supports large text files for efficient parsing  
✅ Uses regex-based pattern matching for accurate IOC extraction  
✅ Outputs results in a structured **tabular format**  
✅ Helps in **malware analysis, threat hunting, and incident response**  

---

## Installation
### Prerequisites
Ensure you have Python installed (Version **3.x** recommended). Install dependencies using:
```bash
pip install tabulate
```

---

## Usage
Run the script with a file containing text to extract IOCs:
```bash
python extract_artifacts.py <input_file>
```
### Example:
```bash
python extract_artifacts.py logs.txt
```

#### Sample Output:
```
#############################################################
  ______ _   _  __
 |  ____| | | |/ /  ___  _  _   _   _   _           
 | |__  | | | ' /  / _ \| '_ \/\ \ | | | |
 |  __| | | |  <  | (_) | | | | | || |_| |  
 | |____| | | . \  \___/|_| |_| |_| \__, |  
 |______|_| |_|\_\                  ___| |
                                   |_____|
#############################################################

==> Extracting Artifacts - By k0my <==
==================================================

IP Addresses:
+----+-----------------+
| #  | IP Address     |
+----+-----------------+
| 1  | 192.168.1.100  |
| 2  | 10.0.0.25      |
+----+-----------------+

Email Addresses:
+----+----------------------+
| #  | Email Address       |
+----+----------------------+
| 1  | test@example.com    |
| 2  | admin@security.com  |
+----+----------------------+
```

---

## Regex Patterns Used
The tool uses the following regex patterns to extract IOCs:
| Category                | Regular Expression |
|-------------------------|--------------------|
| **IP Addresses**        | `\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b` |
| **Email Addresses**     | `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` |
| **URLs**               | `https?://[^\s"']+` |
| **Executable Files**    | `(?:[A-Za-z]:\\|/)?(?:[\w\-\.]+[\\/])*[\w\-\.]+\.(?:exe|bat|bin|sh|ps1|scr|cmd)` |
| **Windows Registry Keys** | `HKEY_LOCAL_MACHINE\\[\w\\]+` |
| **MD5 Hashes**         | `\b[a-fA-F0-9]{32}\b` |
| **SHA-1 Hashes**       | `\b[a-fA-F0-9]{40}\b` |
| **SHA-256 Hashes**     | `\b[a-fA-F0-9]{64}\b` |

---




## Contact
👤 **Author**: k0my  
📧 **Email**: alkomyy22@gmail.com  
🔗 **LinkedIn**: (https://www.linkedin.com/in/ahmed-elkomy-b17946256/)

