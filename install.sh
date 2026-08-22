#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
#  AI TOOLS LAUNCHER - Installation Script
#  Version: 3.0.0
#  Developer: Raj Gautam
#  University: VBSPU, Jaunpur
#  License: MIT
#  Repository: https://github.com/Rg100152/Ai-tools
# ═══════════════════════════════════════════════════════════════════

# Exit on error
set -e

# Color Definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
BRIGHT_RED='\033[0;91m'
BRIGHT_GREEN='\033[0;92m'
BRIGHT_YELLOW='\033[1;93m'
BRIGHT_BLUE='\033[0;94m'
BRIGHT_MAGENTA='\033[0;95m'
BRIGHT_CYAN='\033[0;96m'
NC='\033[0m' # No Color
BOLD='\033[1m'
DIM='\033[2m'

# Installation directories
INSTALL_DIR="$HOME/.local/share/ai-tools"
BIN_DIR="$HOME/.local/bin"
CONFIG_DIR="$HOME/.config/ai-tools"
DATA_DIR="$HOME/.local/share/ai-tools/data"
BACKUP_DIR="$HOME/.local/share/ai-tools/backups"
LOG_DIR="$HOME/.local/share/ai-tools/logs"

# Version
VERSION="3.0.0"

# ═══════════════════════════════════════════════════════════════════
#  DISPLAY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

display_banner() {
    clear
    echo -e "${BRIGHT_RED}${BOLD}╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BRIGHT_RED}║${BRIGHT_CYAN}  █████╗ ██╗    ████████╗ ██████╗  ██████╗ ██╗          ${BRIGHT_RED}║${NC}"
    echo -e "${BRIGHT_RED}║${BRIGHT_CYAN} ██╔══██╗██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║          ${BRIGHT_RED}║${NC}"
    echo -e "${BRIGHT_RED}║${BRIGHT_CYAN} ███████║██║       ██║   ██║   ██║██║   ██║██║          ${BRIGHT_RED}║${NC}"
    echo -e "${BRIGHT_RED}║${BRIGHT_CYAN} ██╔══██║██║       ██║   ██║   ██║██║   ██║██║          ${BRIGHT_RED}║${NC}"
    echo -e "${BRIGHT_RED}║${BRIGHT_CYAN} ██║  ██║███████╗  ██║   ╚██████╔╝╚██████╔╝███████╗     ${BRIGHT_RED}║${NC}"
    echo -e "${BRIGHT_RED}║${BRIGHT_CYAN} ╚═╝  ╚═╝╚══════╝  ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝     ${BRIGHT_RED}║${NC}"
    echo -e "${BRIGHT_RED}╠══════════════════════════════════════════════════════════════════╣${NC}"
    echo -e "${BRIGHT_RED}║${WHITE}      INSTALLATION WIZARD - AI TOOLS LAUNCHER v${VERSION}        ${BRIGHT_RED}║${NC}"
    echo -e "${BRIGHT_RED}║${BRIGHT_YELLOW}      ⚡ Powered by Raj Gautam | VBSPU Jaunpur ⚡             ${BRIGHT_RED}║${NC}"
    echo -e "${BRIGHT_RED}╚══════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

loading_animation() {
    local message="$1"
    local duration="${2:-2}"
    local end=$((SECONDS + duration))
    
    while [ $SECONDS -lt $end ]; do
        for frame in "⠋" "⠙" "⠹" "⠸" "⠼" "⠴" "⠦" "⠧" "⠇" "⠏"; do
            printf "\r${CYAN}[${frame}] ${WHITE}${message}${NC} "
            sleep 0.1
        done
    done
    printf "\r${GREEN}[✓] ${WHITE}${message} - Done!${NC}                    \n"
}

# ═══════════════════════════════════════════════════════════════════
#  CHECK FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

check_root() {
    if [[ $EUID -eq 0 ]]; then
        echo -e "${RED}[✗] ${WHITE}Please don't run as root!${NC}"
        echo -e "${YELLOW}[*] ${WHITE}This script installs to user directory only${NC}"
        exit 1
    fi
}

check_os() {
    echo -e "${CYAN}[*] ${WHITE}Checking operating system...${NC}"
    
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo -e "${GREEN}[✓] ${WHITE}Linux detected${NC}"
        OS_TYPE="linux"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo -e "${GREEN}[✓] ${WHITE}macOS detected${NC}"
        OS_TYPE="macos"
    elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]]; then
        echo -e "${GREEN}[✓] ${WHITE}Windows (Cygwin/MSYS) detected${NC}"
        OS_TYPE="windows"
    else
        echo -e "${RED}[✗] ${WHITE}Unsupported OS: $OSTYPE${NC}"
        exit 1
    fi
}

check_python() {
    echo -e "${CYAN}[*] ${WHITE}Checking Python...${NC}"
    
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
        echo -e "${GREEN}[✓] ${WHITE}Python3 found: ${CYAN}$PYTHON_VERSION${NC}"
        
        # Check version
        if python3 -c "import sys; exit(0 if sys.version_info >= (3, 6) else 1)"; then
            echo -e "${GREEN}[✓] ${WHITE}Python version compatible (3.6+)${NC}"
        else
            echo -e "${RED}[✗] ${WHITE}Python 3.6+ required!${NC}"
            echo -e "${YELLOW}[*] ${WHITE}Installing Python...${NC}"
            install_python
        fi
    else
        echo -e "${RED}[✗] ${WHITE}Python3 not found!${NC}"
        echo -e "${YELLOW}[*] ${WHITE}Installing Python...${NC}"
        install_python
    fi
}

install_python() {
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y python3 python3-pip
    elif command -v yum &> /dev/null; then
        sudo yum install -y python3 python3-pip
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y python3 python3-pip
    elif command -v pacman &> /dev/null; then
        sudo pacman -S python python-pip
    elif command -v brew &> /dev/null; then
        brew install python3
    else
        echo -e "${RED}[✗] ${WHITE}Please install Python3 manually${NC}"
        exit 1
    fi
}

check_git() {
    echo -e "${CYAN}[*] ${WHITE}Checking Git...${NC}"
    
    if command -v git &> /dev/null; then
        GIT_VERSION=$(git --version | awk '{print $3}')
        echo -e "${GREEN}[✓] ${WHITE}Git found: ${CYAN}$GIT_VERSION${NC}"
    else
        echo -e "${YELLOW}[!] ${WHITE}Git not found (optional)${NC}"
    fi
}

check_browser() {
    echo -e "${CYAN}[*] ${WHITE}Checking browser...${NC}"
    
    if command -v xdg-open &> /dev/null; then
        echo -e "${GREEN}[✓] ${WHITE}xdg-open found${NC}"
    elif command -v open &> /dev/null; then
        echo -e "${GREEN}[✓] ${WHITE}open command found${NC}"
    else
        echo -e "${YELLOW}[!] ${WHITE}No default browser opener found${NC}"
    fi
}

# ═══════════════════════════════════════════════════════════════════
#  INSTALL FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

create_directories() {
    echo -e "${CYAN}[*] ${WHITE}Creating directories...${NC}"
    
    mkdir -p "$INSTALL_DIR"
    mkdir -p "$BIN_DIR"
    mkdir -p "$CONFIG_DIR"
    mkdir -p "$DATA_DIR"
    mkdir -p "$BACKUP_DIR"
    mkdir -p "$LOG_DIR"
    
    echo -e "${GREEN}[✓] ${WHITE}Directories created${NC}"
}

copy_files() {
    echo -e "${CYAN}[*] ${WHITE}Copying files...${NC}"
    
    # Get script directory
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    
    # Copy Python script
    if [ -f "$SCRIPT_DIR/ai_tool.py" ]; then
        cp "$SCRIPT_DIR/ai_tool.py" "$INSTALL_DIR/"
        echo -e "${GREEN}[✓] ${WHITE}ai_tool.py copied${NC}"
    else
        echo -e "${YELLOW}[!] ${WHITE}ai_tool.py not found in current directory${NC}"
        echo -e "${YELLOW}[*] ${WHITE}Downloading from GitHub...${NC}"
        download_from_github
    fi
    
    # Copy config files
    if [ -f "$SCRIPT_DIR/config.json" ]; then
        cp "$SCRIPT_DIR/config.json" "$CONFIG_DIR/"
        echo -e "${GREEN}[✓] ${WHITE}config.json copied${NC}"
    fi
    
    # Copy database files
    if [ -f "$SCRIPT_DIR/tools_database.json" ]; then
        cp "$SCRIPT_DIR/tools_database.json" "$DATA_DIR/"
        echo -e "${GREEN}[✓] ${WHITE}tools_database.json copied${NC}"
    fi
}

download_from_github() {
    echo -e "${CYAN}[*] ${WHITE}Downloading from GitHub...${NC}"
    
    if command -v git &> /dev/null; then
        git clone https://github.com/Rg100152/Ai-tools.git "$INSTALL_DIR/temp"
        cp "$INSTALL_DIR/temp/ai_tool.py" "$INSTALL_DIR/"
        rm -rf "$INSTALL_DIR/temp"
        echo -e "${GREEN}[✓] ${WHITE}Downloaded successfully${NC}"
    else
        echo -e "${RED}[✗] ${WHITE}Git not available for download${NC}"
        echo -e "${YELLOW}[*] ${WHITE}Please download manually from GitHub${NC}"
        exit 1
    fi
}

create_wrapper() {
    echo -e "${CYAN}[*] ${WHITE}Creating executable wrapper...${NC}"
    
    cat > "$BIN_DIR/ai-tools" << 'EOF'
#!/bin/bash
# AI Tools Launcher - Wrapper Script

INSTALL_DIR="$HOME/.local/share/ai-tools"
CONFIG_DIR="$HOME/.config/ai-tools"

# Run the main script
python3 "$INSTALL_DIR/ai_tool.py" "$@"
EOF
    
    chmod +x "$BIN_DIR/ai-tools"
    echo -e "${GREEN}[✓] ${WHITE}Wrapper created at ${CYAN}$BIN_DIR/ai-tools${NC}"
}

create_desktop_entry() {
    echo -e "${CYAN}[*] ${WHITE}Creating desktop entry...${NC}"
    
    DESKTOP_DIR="$HOME/.local/share/applications"
    mkdir -p "$DESKTOP_DIR"
    
    cat > "$DESKTOP_DIR/ai-tools.desktop" << EOF
[Desktop Entry]
Name=AI Tools Launcher
Comment=Launch 120+ AI tools from terminal
Exec=$BIN_DIR/ai-tools
Icon=terminal
Terminal=true
Type=Application
Categories=Utility;Development;
Keywords=AI;Tools;Launcher;
EOF
    
    echo -e "${GREEN}[✓] ${WHITE}Desktop entry created${NC}"
}

add_to_path() {
    echo -e "${CYAN}[*] ${WHITE}Adding to PATH...${NC}"
    
    if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
        # Add to .bashrc
        if [ -f "$HOME/.bashrc" ]; then
            echo "export PATH=\"$BIN_DIR:\$PATH\"" >> "$HOME/.bashrc"
            echo -e "${GREEN}[✓] ${WHITE}Added to .bashrc${NC}"
        fi
        
        # Add to .zshrc
        if [ -f "$HOME/.zshrc" ]; then
            echo "export PATH=\"$BIN_DIR:\$PATH\"" >> "$HOME/.zshrc"
            echo -e "${GREEN}[✓] ${WHITE}Added to .zshrc${NC}"
        fi
        
        # Add to .profile
        if [ -f "$HOME/.profile" ]; then
            echo "export PATH=\"$BIN_DIR:\$PATH\"" >> "$HOME/.profile"
            echo -e "${GREEN}[✓] ${WHITE}Added to .profile${NC}"
        fi
    else
        echo -e "${GREEN}[✓] ${WHITE}Already in PATH${NC}"
    fi
}

create_config() {
    echo -e "${CYAN}[*] ${WHITE}Creating default config...${NC}"
    
    if [ ! -f "$CONFIG_DIR/config.json" ]; then
        cat > "$CONFIG_DIR/config.json" << 'EOF'
{
  "app_name": "AI Tools Launcher",
  "version": "3.0.0",
  "theme": "matrix",
  "show_price": true,
  "show_description": true,
  "animation_speed": "fast",
  "browser": "default",
  "max_history": 20
}
EOF
        echo -e "${GREEN}[✓] ${WHITE}Default config created${NC}"
    else
        echo -e "${GREEN}[✓] ${WHITE}Config already exists${NC}"
    fi
}

create_data_files() {
    echo -e "${CYAN}[*] ${WHITE}Creating data files...${NC}"
    
    # Create empty favorites file
    if [ ! -f "$DATA_DIR/favorites.json" ]; then
        echo '{"version": "1.0.0", "favorites": []}' > "$DATA_DIR/favorites.json"
    fi
    
    # Create empty history file
    if [ ! -f "$DATA_DIR/history.json" ]; then
        echo '{"version": "1.0.0", "history": []}' > "$DATA_DIR/history.json"
    fi
    
    echo -e "${GREEN}[✓] ${WHITE}Data files created${NC}"
}

create_alias() {
    echo -e "${CYAN}[*] ${WHITE}Creating alias...${NC}"
    
    if [ -f "$HOME/.bashrc" ]; then
        # Remove old alias if exists
        sed -i '/alias ai-tools=/d' "$HOME/.bashrc"
        # Add new alias
        echo "alias ai-tools='$BIN_DIR/ai-tools'" >> "$HOME/.bashrc"
        echo -e "${GREEN}[✓] ${WHITE}Alias created${NC}"
    fi
}

set_permissions() {
    echo -e "${CYAN}[*] ${WHITE}Setting permissions...${NC}"
    
    chmod +x "$INSTALL_DIR/ai_tool.py" 2>/dev/null || true
    chmod +x "$BIN_DIR/ai-tools"
    
    echo -e "${GREEN}[✓] ${WHITE}Permissions set${NC}"
}

verify_installation() {
    echo -e "${CYAN}[*] ${WHITE}Verifying installation...${NC}"
    
    if [ -f "$INSTALL_DIR/ai_tool.py" ]; then
        echo -e "${GREEN}[✓] ${WHITE}Main script installed${NC}"
    else
        echo -e "${RED}[✗] ${WHITE}Main script missing!${NC}"
        return 1
    fi
    
    if [ -f "$BIN_DIR/ai-tools" ]; then
        echo -e "${GREEN}[✓] ${WHITE}Executable installed${NC}"
    else
        echo -e "${RED}[✗] ${WHITE}Executable missing!${NC}"
        return 1
    fi
    
    if [ -f "$CONFIG_DIR/config.json" ]; then
        echo -e "${GREEN}[✓] ${WHITE}Config installed${NC}"
    else
        echo -e "${YELLOW}[!] ${WHITE}Config missing (will create on first run)${NC}"
    fi
    
    return 0
}

# ═══════════════════════════════════════════════════════════════════
#  UNINSTALL FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

uninstall() {
    echo -e "${RED}[!] ${WHITE}Are you sure you want to uninstall? (y/n)${NC}"
    read -p "> " confirm
    
    if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
        echo -e "${CYAN}[*] ${WHITE}Uninstalling...${NC}"
        
        # Remove executable
        rm -f "$BIN_DIR/ai-tools"
        echo -e "${GREEN}[✓] ${WHITE}Removed executable${NC}"
        
        # Remove install directory
        rm -rf "$INSTALL_DIR"
        echo -e "${GREEN}[✓] ${WHITE}Removed install directory${NC}"
        
        # Remove config
        rm -rf "$CONFIG_DIR"
        echo -e "${GREEN}[✓] ${WHITE}Removed config${NC}"
        
        # Remove desktop entry
        rm -f "$HOME/.local/share/applications/ai-tools.desktop"
        echo -e "${GREEN}[✓] ${WHITE}Removed desktop entry${NC}"
        
        # Remove alias from .bashrc
        sed -i '/alias ai-tools=/d' "$HOME/.bashrc"
        echo -e "${GREEN}[✓] ${WHITE}Removed alias${NC}"
        
        echo -e "${GREEN}[✓] ${WHITE}Uninstallation complete!${NC}"
        exit 0
    else
        echo -e "${YELLOW}[*] ${WHITE}Uninstallation cancelled${NC}"
        exit 0
    fi
}

# ═══════════════════════════════════════════════════════════════════
#  UPDATE FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

update() {
    echo -e "${CYAN}[*] ${WHITE}Updating AI Tools Launcher...${NC}"
    
    if command -v git &> /dev/null; then
        cd "$INSTALL_DIR"
        git pull origin main 2>/dev/null && {
            echo -e "${GREEN}[✓] ${WHITE}Updated successfully!${NC}"
        } || {
            echo -e "${RED}[✗] ${WHITE}Update failed${NC}"
        }
    else
        echo -e "${RED}[✗] ${WHITE}Git not installed!${NC}"
    fi
}

# ═══════════════════════════════════════════════════════════════════
#  MAIN INSTALLATION
# ═══════════════════════════════════════════════════════════════════

main_install() {
    display_banner
    
    echo -e "${CYAN}${BOLD}╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${WHITE}                    INSTALLATION PROCESS                      ${CYAN}║${NC}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    
    # Check system
    check_root
    check_os
    check_python
    check_git
    check_browser
    
    echo ""
    echo -e "${CYAN}${BOLD}╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${WHITE}                      INSTALLING FILES                      ${CYAN}║${NC}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    
    # Install
    loading_animation "Creating directories" 1
    create_directories
    
    loading_animation "Copying files" 1
    copy_files
    
    loading_animation "Creating wrapper" 1
    create_wrapper
    
    loading_animation "Creating desktop entry" 1
    create_desktop_entry
    
    loading_animation "Adding to PATH" 1
    add_to_path
    
    loading_animation "Creating config" 1
    create_config
    
    loading_animation "Creating data files" 1
    create_data_files
    
    loading_animation "Creating alias" 1
    create_alias
    
    loading_animation "Setting permissions" 1
    set_permissions
    
    echo ""
    echo -e "${CYAN}${BOLD}╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${WHITE}                      VERIFICATION                            ${CYAN}║${NC}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    
    if verify_installation; then
        echo ""
        echo -e "${GREEN}${BOLD}╔══════════════════════════════════════════════════════════════════╗${NC}"
        echo -e "${GREEN}║${WHITE}                  INSTALLATION COMPLETE! 🎉                  ${GREEN}║${NC}"
        echo -e "${GREEN}╚══════════════════════════════════════════════════════════════════╝${NC}"
        echo ""
        echo -e "${YELLOW}[*] ${WHITE}To start using AI Tools Launcher:${NC}"
        echo -e "${CYAN}   1. Restart terminal or run: ${WHITE}source ~/.bashrc${NC}"
        echo -e "${CYAN}   2. Type: ${WHITE}ai-tools${NC}"
        echo ""
        echo -e "${YELLOW}[*] ${WHITE}Available commands:${NC}"
        echo -e "${CYAN}   ai-tools${NC}              ${WHITE}Launch the tool${NC}"
        echo -e "${CYAN}   ai-tools --help${NC}       ${WHITE}Show help${NC}"
        echo -e "${CYAN}   ai-tools --version${NC}    ${WHITE}Show version${NC}"
        echo -e "${CYAN}   ai-tools --update${NC}     ${WHITE}Update from GitHub${NC}"
        echo -e "${CYAN}   ai-tools --uninstall${NC}  ${WHITE}Uninstall${NC}"
        echo ""
        echo -e "${GREEN}[✓] ${WHITE}Thank you for installing!${NC}"
        echo -e "${GREEN}[✓] ${WHITE}Developer: Raj Gautam | VBSPU Jaunpur${NC}"
        echo ""
    else
        echo -e "${RED}[✗] ${WHITE}Installation failed!${NC}"
        exit 1
    fi
}

# ═══════════════════════════════════════════════════════════════════
#  MAIN PROGRAM
# ═══════════════════════════════════════════════════════════════════

# Handle command line arguments
case "$1" in
    --uninstall|-u)
        uninstall
        ;;
    --update|--upgrade)
        update
        ;;
    --help|-h)
        echo "AI Tools Launcher - Installation Script"
        echo "Usage: $0 [OPTIONS]"
        echo ""
        echo "Options:"
        echo "  --install     Install AI Tools Launcher (default)"
        echo "  --uninstall   Uninstall AI Tools Launcher"
        echo "  --update      Update from GitHub"
        echo "  --help        Show this help"
        echo ""
        exit 0
        ;;
    --version|-v)
        echo "AI Tools Launcher v$VERSION"
        exit 0
        ;;
    *)
        main_install
        ;;
esac
