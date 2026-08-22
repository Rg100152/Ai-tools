
# 🤖 AI Tools Launcher v3.0.0

<div align="center">

![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.6%2B-yellow.svg)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Termux%20%7C%20Debian-red.svg)
![GitHub stars](https://img.shields.io/github/stars/Rg100152/Ai-tools?style=social)

**A powerful CLI-based AI tools launcher with 120+ AI platforms, hacker-style interface, and lightning-fast access.**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Commands](#-commands) • [Developer](#-developer)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Installation](#-installation)
  - [Debian/Ubuntu](#-debianubuntu)
  - [Termux (Android)](#-termux-android)
  - [Arch Linux](#-arch-linux)
  - [Fedora](#-fedora)
  - [macOS](#-macos)
  - [Windows](#-windows)
- [Usage](#-usage)
- [Commands](#-commands)
- [Configuration](#-configuration)
- [File Structure](#-file-structure)
- [Contributing](#-contributing)
- [License](#-license)
- [Developer](#-developer)

---

## 📖 Overview

AI Tools Launcher is a powerful command-line interface (CLI) tool that provides instant access to 120+ AI platforms and tools. Built with Python and Bash, it features a hacker-style interface with matrix effects, animations, and comprehensive tool management.

### Why AI Tools Launcher?

- 🚀 **Fast Access** - Launch any AI tool in seconds
- 🎯 **Organized** - Categorized and searchable database
- 💾 **Track Usage** - History and favorites system
- 🎨 **Beautiful UI** - Colorful terminal interface
- 🔧 **Customizable** - Themes and configurations
- 📱 **Cross-Platform** - Works on any terminal

---

## ✨ Features

### Core Features

- 🎯 **120+ AI Tools** - Chat, Image, Video, Code, Music, and more
- 🎨 **Hacker-Style UI** - Matrix effects and animations
- 📂 **Category Browser** - 16 categories with icons
- ❤️ **Favorites System** - Save and organize favorite tools
- 📜 **History Tracking** - Track usage patterns
- 🔍 **Smart Search** - Find tools by name, type, or description
- 🎲 **Random Picker** - Discover new tools daily
- 🚀 **One-Key Launch** - Open any tool instantly

### Advanced Features

- ⚡ **Quick Access Menu** - 10 most popular tools
- 📊 **Statistics** - Usage analytics and insights
- 🎭 **Multiple Themes** - 5 color themes
- 🔄 **Auto-Update** - Stay current with GitHub
- 💾 **Export/Import** - JSON, CSV formats
- 🔔 **Notifications** - Desktop notifications
- 📝 **Notes System** - Add notes to tools
- 🏷️ **Custom Tags** - Organize with tags
- 📌 **Pin Tools** - Pin important tools
- 🔑 **Keyboard Shortcuts** - Fast navigation

---

## 🖼️ Screenshots

### Main Interface
```

╔══════════════════════════════════════════════════════════════════╗
║  █████╗ ██╗    ████████╗ ██████╗  ██████╗ ██╗          ║
║ ██╔══██╗██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║          ║
║ ███████║██║       ██║   ██║   ██║██║   ██║██║          ║
║ ██╔══██║██║       ██║   ██║   ██║██║   ██║██║          ║
║ ██║  ██║███████╗  ██║   ╚██████╔╝╚██████╔╝███████╗     ║
║ ╚═╝  ╚═╝╚══════╝  ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝     ║
╠══════════════════════════════════════════════════════════════════╣
║       120+ AI TOOLS LAUNCHER v3.0.0 - LINUX EDITION          ║
║      ⚡ Powered by Raj Gautam | VBSPU Jaunpur ⚡             ║
╚══════════════════════════════════════════════════════════════════╝

```

### Quick Access Menu
```

┌──────────────────────────────────────────────────────────────────┐
│                    AI TOOLS QUICK ACCESS                        │
└──────────────────────────────────────────────────────────────────┘

Quick Access Tools:
──────────────────────────────────────────────────────────────────
[1] DeepSeek AI (Chat)
[2] ChatGPT (Chat)
[3] Claude AI (Chat)
[4] Google Gemini (Chat)
[5] Midjourney (Image)
[6] GitHub Copilot (Code)
[7] Hugging Face (Dev)
[8] Perplexity (Search)
[9] Suno AI (Music)
[10] ElevenLabs (Voice)

```

---

## 📥 Installation

### 🐧 Debian/Ubuntu

#### Method 1: One-Liner Install (Recommended)
```bash
curl -sSL https://raw.githubusercontent.com/Rg100152/Ai-tools/main/install.sh | bash
```

Method 2: Manual Install

```bash
# Update system
sudo apt-get update
sudo apt-get upgrade -y

# Install dependencies
sudo apt-get install -y python3 python3-pip git

# Clone repository
git clone https://github.com/Rg100152/Ai-tools.git
cd Ai-tools

# Run installer
chmod +x install.sh
./install.sh

# Refresh shell
source ~/.bashrc
```

Method 3: Direct Download

```bash
# Download script
wget https://raw.githubusercontent.com/Rg100152/Ai-tools/main/ai_tool.py
wget https://raw.githubusercontent.com/Rg100152/Ai-tools/main/config.json

# Make executable
chmod +x ai_tool.py

# Run directly
python3 ai_tool.py
```

📱 Termux (Android)

Installation

```bash
# Update Termux
pkg update && pkg upgrade -y

# Install dependencies
pkg install python git curl -y
pkg install python-pip -y

# Clone repository
git clone https://github.com/Rg100152/Ai-tools.git
cd Ai-tools

# Run installer
chmod +x install.sh
./install.sh

# Or run directly
python3 ai_tool.py
```

Termux-Specific Setup

```bash
# Give storage permission
termux-setup-storage

# Install browser (if needed)
pkg install termux-api -y

# For better experience
pkg install ncurses-utils -y
```

🐧 Arch Linux

```bash
# Install dependencies
sudo pacman -S python python-pip git

# Install from AUR (if available)
yay -S ai-tools-launcher

# Or manual install
git clone https://github.com/Rg100152/Ai-tools.git
cd Ai-tools
chmod +x install.sh
./install.sh
```

🎩 Fedora

```bash
# Install dependencies
sudo dnf install python3 python3-pip git

# Clone and install
git clone https://github.com/Rg100152/Ai-tools.git
cd Ai-tools
chmod +x install.sh
./install.sh
```

🍎 macOS

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install python3 git

# Clone and install
git clone https://github.com/Rg100152/Ai-tools.git
cd Ai-tools
chmod +x install.sh
./install.sh
```

🪟 Windows

Method 1: WSL (Recommended)

```bash
# Install WSL
wsl --install

# Open WSL and follow Debian/Ubuntu instructions
```

Method 2: Git Bash

```bash
# Download Git for Windows
# Open Git Bash and run:
git clone https://github.com/Rg100152/Ai-tools.git
cd Ai-tools
python ai_tool.py
```

---

🚀 Usage

Basic Usage

```bash
# Start the launcher
ai-tools

# Or if not installed
python3 ai_tool.py

# Or with shell script
./ai_tool.sh
```

Command Line Arguments

```bash
ai-tools --help          # Show help
ai-tools --version       # Show version
ai-tools --update        # Update from GitHub
ai-tools --uninstall     # Uninstall
ai-tools --info          # Developer info
ai-tools --search "code" # Search tools
```

Inside the Program

```bash
# Navigation
[N] - Next page
[P] - Previous page
[C] - Browse categories
[S] - Search tools
[F] - View favorites
[H] - View history
[R] - Random tool
[?] - Help menu
[99] - Developer info
[0] - Exit

# Quick Access
[1-10] - Open quick access tools

# Direct Access
[1-120] - Open tool by ID
```

---

📋 Commands

Keyboard Shortcuts

Key Command Description
1-10 Quick Access Open popular tools
1-120 Direct Access Open tool by ID
N Next Page Navigate forward
P Previous Page Navigate backward
C Categories Browse by category
S Search Search tools
F Favorites View favorites
H History View history
R Random Random tool
? Help Show help
99 Info Developer info
0 Exit Exit program

Search Operators

```bash
# Search by name
s
> chatgpt

# Search by type
s
> code assistant

# Search by description
s
> image generation

# Search by price
s
> free
```

---

⚙️ Configuration

Config File Location

```bash
# Linux
~/.config/ai-tools/config.json

# Termux
~/.config/ai-tools/config.json

# macOS
~/.config/ai-tools/config.json
```

Config Options

```json
{
  "theme": "matrix",           // matrix, cyberpunk, blood, ocean, forest
  "animation_speed": "fast",   // slow, normal, fast, ultra
  "show_price": true,
  "show_description": true,
  "browser": "default",        // default, chrome, firefox, brave
  "max_history": 20,
  "max_favorites": 50
}
```

Themes

Theme Colors Description
matrix Green/Black Classic Matrix style
cyberpunk Magenta/Cyan Cyberpunk style
blood Red/Black Dark red theme
ocean Blue/Cyan Ocean blue theme
forest Green/Yellow Forest theme

---

📁 File Structure

```
Ai-tools/
├── ai_tool.py              # Main Python script
├── ai_tool.sh              # Shell wrapper script
├── install.sh              # Installation script
├── config.json             # Configuration file
├── tools_database.json     # AI tools database
├── favorites.json          # Favorites storage
├── history.json            # History tracking
├── history_manager.py      # History management
├── favorites_manager.py    # Favorites management
├── README.md               # Documentation
├── LICENSE                 # MIT License
├── .gitignore              # Git ignore file
└── screenshots/            # Screenshots
    ├── main.png
    ├── categories.png
    └── search.png
```

---

🛠️ Development

Prerequisites

```bash
# Required
python3 >= 3.6
git

# Optional
pip3
curl
wget
```

Setup Development Environment

```bash
# Clone repository
git clone https://github.com/Rg100152/Ai-tools.git
cd Ai-tools

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install development dependencies
pip install -r requirements.txt

# Run tests
python3 -m pytest tests/
```

Building

```bash
# Create executable
chmod +x ai_tool.py

# Create package
tar -czf ai-tools-v3.0.0.tar.gz Ai-tools/

# Create Debian package
dpkg-buildpackage -us -uc
```

---

🤝 Contributing

Contributions are welcome! Here's how you can help:

Ways to Contribute

1. 🐛 Report Bugs - Open an issue
2. 💡 Suggest Features - Share ideas
3. 📝 Improve Documentation - Fix typos
4. 🌐 Add Tools - Add new AI tools to database
5. 🎨 Create Themes - Design new color schemes
6. 🔧 Fix Code - Submit pull requests

Contribution Guidelines

```bash
# Fork repository
# Create feature branch
git checkout -b feature/amazing-feature

# Commit changes
git commit -m "Add amazing feature"

# Push to branch
git push origin feature/amazing-feature

# Open pull request
```

---

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

```
MIT License

Copyright (c) 2024 Raj Gautam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

👨‍💻 Developer

<div align="center">

Raj Gautam

BCA Student | VBSPU, Jaunpur

https://img.shields.io/badge/GitHub-Rg100152-black?style=for-the-badge&logo=github
https://img.shields.io/badge/Email-rajgautam.dev%40gmail.com-red?style=for-the-badge&logo=gmail

</div>

Core Skills

· 💻 Software & Web Development
· 🐍 Python Programming
· 🌐 HTML, CSS & JavaScript
· 🤖 Artificial Intelligence & AI Tools
· 🔐 Cybersecurity & Ethical Security Research
· 🐧 Linux & Open-Source Technologies

Philosophy

"Learn. Build. Experiment. Improve."

---

🙏 Acknowledgments

· All AI tool providers
· Open source community
· VBSPU, Jaunpur
· Contributors and testers

---

📊 Statistics

https://img.shields.io/github/stars/Rg100152/Ai-tools?style=social
https://img.shields.io/github/forks/Rg100152/Ai-tools?style=social
https://img.shields.io/github/issues/Rg100152/Ai-tools
https://img.shields.io/github/issues-pr/Rg100152/Ai-tools
https://img.shields.io/github/last-commit/Rg100152/Ai-tools

---

🚀 Quick Start

```bash
# One-liner install
curl -sSL https://raw.githubusercontent.com/Rg100152/Ai-tools/main/install.sh | bash

# Start using
ai-tools

# That's it! 🎉
```

---

<div align="center">

Made with ❤️ by Raj Gautam

"The best way to learn technology is to build, break, understand, and improve."

</div>
```

