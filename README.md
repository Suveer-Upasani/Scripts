# Scirpts

A collection of scripts and automations designed to simplify and automate various tasks. This repository focuses on security tools automation and general utility scripts.

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Scripts](#scripts)
  - [FFUF Automation](#ffuf-automation)
- [Contributing](#contributing)

## Overview
This repository serves as a centralized hub for automation scripts. The goal is to provide a clean, deployable codebase for recurring tasks, starting with security-focused scanning automations.

## Project Structure
```text
.
├── Fuff/           # FFUF automation scripts
├── Wordlist/       # Common wordlists used by scanners
├── results/        # (Ignored) Directory for scan results
└── venv/           # (Ignored) Python virtual environment
```

## Getting Started

### Prerequisites
- Python 3.12+
- [FFUF](https://github.com/ffuf/ffuf) installed and in your PATH.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/scirpts.git
   cd scirpts
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   ```

## Scripts

### FFUF Automation
Located in `Fuff/simple.py`, this script automates directory fuzzing using `ffuf`.
- **Targets:** Configurable list of URLs.
- **Wordlist:** Uses `Wordlist/common.txt`.
- **Output:** Saves results as JSON in the `results/` directory.

To run:
```bash
python Fuff/simple.py
```

## Deployment
This repository is configured with a `.gitignore` to ensure that virtual environments and sensitive result files are not pushed to GitHub.

---
*Maintained for automation and efficiency.*
