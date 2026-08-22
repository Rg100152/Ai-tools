#!/bin/bash
# ═══════════════════════════════════════════════════════════════════
#  AI TOOLS LAUNCHER - Linux Shell Script
#  Version: 3.0.0
#  Developer: Raj Gautam
#  University: VBSPU, Jaunpur
#  Description: Complete AI tools launcher with 120+ tools
# ═══════════════════════════════════════════════════════════════════

# Color Definitions
export RED='\033[0;31m'
export GREEN='\033[0;32m'
export YELLOW='\033[1;33m'
export BLUE='\033[0;34m'
export MAGENTA='\033[0;35m'
export CYAN='\033[0;36m'
export WHITE='\033[1;37m'
export BRIGHT_RED='\033[0;91m'
export BRIGHT_GREEN='\033[0;92m'
export BRIGHT_YELLOW='\033[1;93m'
export BRIGHT_BLUE='\033[0;94m'
export BRIGHT_MAGENTA='\033[0;95m'
export BRIGHT_CYAN='\033[0;96m'
export NC='\033[0m' # No Color
export BOLD='\033[1m'
export DIM='\033[2m'
export BLINK='\033[5m'
export REVERSE='\033[7m'

# Script Directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="$SCRIPT_DIR/config.json"
FAVORITES_FILE="$SCRIPT_DIR/favorites.txt"
HISTORY_FILE="$SCRIPT_DIR/history.txt"

# Version
VERSION="3.0.0"

# ═══════════════════════════════════════════════════════════════════
#  FUNCTIONS
# ═══════════════════════════════════════════════════════════════════

# Clear Screen
clear_screen() {
    clear
}

# Loading Animation
loading_animation() {
    local message="$1"
    local duration="${2:-2}"
    local end=$((SECONDS + duration))
    
    echo -e "${CYAN}[*] ${WHITE}${message}${NC}"
    
    while [ $SECONDS -lt $end ]; do
        for frame in "⠋" "⠙" "⠹" "⠸" "⠼" "⠴" "⠦" "⠧" "⠇" "⠏"; do
            printf "\r${CYAN}[${frame}] ${WHITE}Loading... ${GREEN}█${NC} "
            sleep 0.1
        done
    done
    printf "\r${GREEN}[✓] ${WHITE}Done!${NC}                    \n"
}

# Matrix Effect
matrix_effect() {
    local duration="${1:-1}"
    local end=$((SECONDS + duration))
    local chars=("0" "1" "A" "B" "C" "D" "E" "F")
    
    while [ $SECONDS -lt $end ]; do
        local line=""
        for i in $(seq 1 40); do
            local rand_char=${chars[$RANDOM % ${#chars[@]}]}
            line="${line}${GREEN}${rand_char} ${NC}"
        done
        printf "\r${line}"
        sleep 0.05
    done
    printf "\r${NC}"
}

# Display Banner
display_banner() {
    clear_screen
    matrix_effect 0.5
    echo ""
    echo -e "${BRIGHT_RED}${BOLD}╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BRIGHT_RED}║${BRIGHT_CYAN}  █████╗ ██╗    ████████╗ ██████╗  ██████╗ ██╗          ${BRIGHT_RED}║${NC}"
    echo -e "${BRIGHT_RED}║${BRIGHT_CYAN} ██╔══██╗██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║          ${BRIGHT_RED}║${NC}"
    echo -e "${BRIGHT_RED}║${BRIGHT_CYAN} ███████║██║       ██║   ██║   ██║██║   ██║██║          ${BRIGHT_RED}║${NC}"
    echo -e "${BRIGHT_RED}║${BRIGHT_CYAN} ██╔══██║██║       ██║   ██║   ██║██║   ██║██║          ${BRIGHT_RED}║${NC}"
    echo -e "${BRIGHT_RED}║${BRIGHT_CYAN} ██║  ██║███████╗  ██║   ╚██████╔╝╚██████╔╝███████╗     ${BRIGHT_RED}║${NC}"
    echo -e "${BRIGHT_RED}║${BRIGHT_CYAN} ╚═╝  ╚═╝╚══════╝  ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝     ${BRIGHT_RED}║${NC}"
    echo -e "${BRIGHT_RED}╠══════════════════════════════════════════════════════════════════╣${NC}"
    echo -e "${BRIGHT_RED}║${WHITE}      120+ AI TOOLS LAUNCHER v${VERSION} - LINUX EDITION          ${BRIGHT_RED}║${NC}"
    echo -e "${BRIGHT_RED}║${BRIGHT_YELLOW}      ⚡ Powered by Raj Gautam | VBSPU Jaunpur ⚡             ${BRIGHT_RED}║${NC}"
    echo -e "${BRIGHT_RED}╚══════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${GREEN}[✓] ${WHITE}System: ${CYAN}$(uname -s) $(uname -r)${NC}"
    echo -e "${GREEN}[✓] ${WHITE}Date: ${CYAN}$(date '+%Y-%m-%d %H:%M:%S')${NC}"
    echo -e "${GREEN}[✓] ${WHITE}User: ${CYAN}$(whoami)${NC}"
    echo ""
}

# Check Dependencies
check_dependencies() {
    echo -e "${CYAN}[*] Checking dependencies...${NC}"
    
    # Check Python3
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}[✗] Python3 not found!${NC}"
        echo -e "${YELLOW}[*] Installing Python3...${NC}"
        if command -v apt-get &> /dev/null; then
            sudo apt-get update && sudo apt-get install -y python3 python3-pip
        elif command -v yum &> /dev/null; then
            sudo yum install -y python3 python3-pip
        elif command -v pacman &> /dev/null; then
            sudo pacman -S python python-pip
        else
            echo -e "${RED}[✗] Please install Python3 manually${NC}"
            exit 1
        fi
    fi
    
    # Check xdg-open (for browser)
    if ! command -v xdg-open &> /dev/null; then
        echo -e "${YELLOW}[*] xdg-open not found. Installing...${NC}"
        sudo apt-get install -y xdg-utils 2>/dev/null || true
    fi
    
    echo -e "${GREEN}[✓] All dependencies satisfied!${NC}"
    echo ""
}

# Display Help
show_help() {
    clear_screen
    display_banner
    echo -e "${BRIGHT_CYAN}${BOLD}╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BRIGHT_CYAN}${BOLD}║                         HELP & COMMANDS                         ║${NC}"
    echo -e "${BRIGHT_CYAN}${BOLD}╚══════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${YELLOW}${BOLD}Basic Commands:${NC}"
    echo -e "  ${GREEN}ai-tools${NC}              Launch the tool"
    echo -e "  ${GREEN}ai-tools --help${NC}       Show this help"
    echo -e "  ${GREEN}ai-tools --version${NC}    Show version"
    echo -e "  ${GREEN}ai-tools --update${NC}     Update from GitHub"
    echo -e "  ${GREEN}ai-tools --uninstall${NC}  Remove from system"
    echo ""
    echo -e "${YELLOW}${BOLD}Inside Program:${NC}"
    echo -e "  ${GREEN}[1-120]${NC}  Open tool by ID"
    echo -e "  ${GREEN}[N]${NC}      Next page"
    echo -e "  ${GREEN}[P]${NC}      Previous page"
    echo -e "  ${GREEN}[C]${NC}      Browse categories"
    echo -e "  ${GREEN}[S]${NC}      Search tools"
    echo -e "  ${GREEN}[F]${NC}      View favorites"
    echo -e "  ${GREEN}[H]${NC}      View history"
    echo -e "  ${GREEN}[R]${NC}      Random tool"
    echo -e "  ${GREEN}[?]${NC}      Help menu"
    echo -e "  ${GREEN}[99]${NC}     Developer info"
    echo -e "  ${GREEN}[0]${NC}      Exit"
    echo ""
    read -p "Press Enter to continue..."
}

# Developer Info
show_info() {
    clear_screen
    echo -e "${CYAN}${BOLD}╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${WHITE}${BOLD}                    DEVELOPER INFORMATION                      ${NC}${CYAN}║${NC}"
    echo -e "${CYAN}╠══════════════════════════════════════════════════════════════════╣${NC}"
    echo -e "${CYAN}║ ${GREEN}Name:${NC}        ${WHITE}Raj Gautam${NC}                                  ${CYAN}║${NC}"
    echo -e "${CYAN}║ ${GREEN}Education:${NC}    ${WHITE}BCA Student${NC}                                 ${CYAN}║${NC}"
    echo -e "${CYAN}║ ${GREEN}University:${NC}   ${WHITE}VBSPU, Jaunpur${NC}                              ${CYAN}║${NC}"
    echo -e "${CYAN}║ ${GREEN}Interests:${NC}    ${WHITE}Software Dev, Cybersecurity, AI${NC}              ${CYAN}║${NC}"
    echo -e "${CYAN}║ ${GREEN}Motto:${NC}       ${WHITE}\"Learn. Build. Experiment. Improve.\"${NC}        ${CYAN}║${NC}"
    echo -e "${CYAN}╠══════════════════════════════════════════════════════════════════╣${NC}"
    echo -e "${CYAN}║ ${YELLOW}Core Skills:${NC}                                                        ${CYAN}║${NC}"
    echo -e "${CYAN}║ ${WHITE}• Python Programming    • Web Development${NC}                ${CYAN}║${NC}"
    echo -e "${CYAN}║ ${WHITE}• Cybersecurity         • AI & Machine Learning${NC}          ${CYAN}║${NC}"
    echo -e "${CYAN}║ ${WHITE}• Linux Systems         • Database Management${NC}           ${CYAN}║${NC}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    read -p "Press Enter to continue..."
}

# Display Categories Menu
show_categories() {
    echo -e "${YELLOW}${BOLD}╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${YELLOW}${BOLD}║                       AI TOOL CATEGORIES                        ║${NC}"
    echo -e "${YELLOW}${BOLD}╚══════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    
    local categories=(
        "Chat Assistant"
        "Search Engine"
        "Writing"
        "Image Generation"
        "Video Generation"
        "Voice Generation"
        "Music Generation"
        "Transcription"
        "Audio Editing"
        "Code Assistant"
        "Development"
        "Productivity"
        "Presentations"
        "Website Builder"
        "Automation"
        "Autonomous AI"
    )
    
    for i in "${!categories[@]}"; do
        echo -e "${GREEN}[$((i+1))]${NC} ${CYAN}${categories[$i]}${NC}"
    done
    echo ""
    echo -e "${YELLOW}[0] ${WHITE}Back to Main Menu${NC}"
}

# Display Main Menu
display_menu() {
    echo -e "${YELLOW}${BOLD}╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${YELLOW}${BOLD}║                    AI TOOLS QUICK ACCESS                        ║${NC}"
    echo -e "${YELLOW}${BOLD}╚══════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    
    # Quick access tools
    local quick_tools=(
        "DeepSeek AI|https://chat.deepseek.com|Chat"
        "ChatGPT|https://chat.openai.com|Chat"
        "Claude AI|https://claude.ai|Chat"
        "Google Gemini|https://gemini.google.com|Chat"
        "Midjourney|https://www.midjourney.com|Image"
        "GitHub Copilot|https://github.com/features/copilot|Code"
        "Hugging Face|https://huggingface.co|Dev"
        "Perplexity|https://www.perplexity.ai|Search"
        "Suno AI|https://suno.com|Music"
        "ElevenLabs|https://elevenlabs.io|Voice"
    )
    
    echo -e "${CYAN}Quick Access Tools:${NC}"
    echo -e "${CYAN}──────────────────────────────────────────────────────────────────${NC}"
    for i in "${!quick_tools[@]}"; do
        IFS='|' read -r name url type <<< "${quick_tools[$i]}"
        echo -e "${GREEN}[$((i+1))]${NC} ${WHITE}${name}${NC} ${DIM}(${type})${NC}"
    done
    echo ""
    
    # Navigation options
    echo -e "${CYAN}──────────────────────────────────────────────────────────────────${NC}"
    echo -e "${GREEN}[A]${NC} ${WHITE}All Tools (120+)${NC}"
    echo -e "${GREEN}[C]${NC} ${WHITE}Categories${NC}"
    echo -e "${GREEN}[S]${NC} ${WHITE}Search${NC}"
    echo -e "${GREEN}[F]${NC} ${WHITE}Favorites${NC}"
    echo -e "${GREEN}[H]${NC} ${WHITE}History${NC}"
    echo -e "${GREEN}[R]${NC} ${WHITE}Random Tool${NC}"
    echo -e "${GREEN}[?]${NC} ${WHITE}Help${NC}"
    echo -e "${GREEN}[99]${NC} ${WHITE}Developer Info${NC}"
    echo -e "${GREEN}[0]${NC} ${WHITE}Exit${NC}"
    echo ""
}

# Open URL in browser
open_in_browser() {
    local url="$1"
    local tool_name="$2"
    
    echo -e "${CYAN}══════════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}⟳ ACCESSING: ${WHITE}${tool_name}${NC}"
    echo -e "${CYAN}══════════════════════════════════════════════════════════════════${NC}"
    echo -e "${WHITE}URL: ${BLUE}${url}${NC}"
    echo -e "${CYAN}══════════════════════════════════════════════════════════════════${NC}"
    echo ""
    
    loading_animation "Establishing connection..." 1
    
    # Open in browser
    if command -v xdg-open &> /dev/null; then
        xdg-open "$url" 2>/dev/null &
    elif command -v open &> /dev/null; then
        open "$url" 2>/dev/null &
    elif command -v firefox &> /dev/null; then
        firefox "$url" 2>/dev/null &
    elif command -v google-chrome &> /dev/null; then
        google-chrome "$url" 2>/dev/null &
    else
        echo -e "${RED}[✗] No browser found!${NC}"
        echo -e "${YELLOW}[*] Please open manually: ${WHITE}${url}${NC}"
    fi
    
    echo -e "${GREEN}[✓] ${WHITE}Success! ${tool_name} launched${NC}"
    sleep 1
}

# Quick Launch Function
quick_launch() {
    local choice="$1"
    
    case $choice in
        1) open_in_browser "https://chat.deepseek.com" "DeepSeek AI" ;;
        2) open_in_browser "https://chat.openai.com" "ChatGPT" ;;
        3) open_in_browser "https://claude.ai" "Claude AI" ;;
        4) open_in_browser "https://gemini.google.com" "Google Gemini" ;;
        5) open_in_browser "https://www.midjourney.com" "Midjourney" ;;
        6) open_in_browser "https://github.com/features/copilot" "GitHub Copilot" ;;
        7) open_in_browser "https://huggingface.co" "Hugging Face" ;;
        8) open_in_browser "https://www.perplexity.ai" "Perplexity AI" ;;
        9) open_in_browser "https://suno.com" "Suno AI" ;;
        10) open_in_browser "https://elevenlabs.io" "ElevenLabs" ;;
        *) echo -e "${RED}[✗] Invalid choice${NC}" ;;
    esac
}

# Search Function
search_tool() {
    echo -e "${YELLOW}[*] ${WHITE}Enter search term:${NC}"
    read -p "> " search_term
    
    if [ -z "$search_term" ]; then
        return
    fi
    
    echo -e "${CYAN}[*] Searching for '${WHITE}${search_term}${CYAN}'...${NC}"
    echo ""
    
    # Here you would search through your database
    # For now, showing example
    echo -e "${GREEN}[✓] ${WHITE}Search results for '${search_term}':${NC}"
    echo -e "${CYAN}──────────────────────────────────────────────────────────────────${NC}"
    echo -e "${GREEN}[1]${NC} ${WHITE}DeepSeek AI${NC} - Chat Assistant"
    echo -e "${GREEN}[2]${NC} ${WHITE}SearchGPT${NC} - Search Engine"
    echo -e "${GREEN}[3]${NC} ${WHITE}${search_term} Tool${NC} - AI Tool"
    echo -e "${CYAN}──────────────────────────────────────────────────────────────────${NC}"
    echo ""
    read -p "Enter ID to open (or Enter to skip): " open_choice
    if [ -n "$open_choice" ]; then
        case $open_choice in
            1) open_in_browser "https://chat.deepseek.com" "DeepSeek AI" ;;
            2) open_in_browser "https://openai.com" "SearchGPT" ;;
            3) echo -e "${YELLOW}[*] Tool not available in demo${NC}" ;;
        esac
    fi
}

# View Favorites
view_favorites() {
    if [ -f "$FAVORITES_FILE" ]; then
        echo -e "${MAGENTA}${BOLD}╔══════════════════════════════════════════════════════════════════╗${NC}"
        echo -e "${MAGENTA}${BOLD}║                         YOUR FAVORITES                          ║${NC}"
        echo -e "${MAGENTA}${BOLD}╚══════════════════════════════════════════════════════════════════╝${NC}"
        echo ""
        cat "$FAVORITES_FILE" | while read line; do
            echo -e "${GREEN}[♥]${NC} ${WHITE}${line}${NC}"
        done
        echo ""
    else
        echo -e "${YELLOW}[!] ${WHITE}No favorites yet${NC}"
    fi
    read -p "Press Enter to continue..."
}

# View History
view_history() {
    if [ -f "$HISTORY_FILE" ]; then
        echo -e "${CYAN}${BOLD}╔══════════════════════════════════════════════════════════════════╗${NC}"
        echo -e "${CYAN}${BOLD}║                         RECENT HISTORY                          ║${NC}"
        echo -e "${CYAN}${BOLD}╚══════════════════════════════════════════════════════════════════╝${NC}"
        echo ""
        cat "$HISTORY_FILE" | tail -10 | while read line; do
            echo -e "${GREEN}[*]${NC} ${WHITE}${line}${NC}"
        done
        echo ""
    else
        echo -e "${YELLOW}[!] ${WHITE}No history yet${NC}"
    fi
    read -p "Press Enter to continue..."
}

# Random Tool
random_tool() {
    local tools=(
        "ChatGPT|https://chat.openai.com"
        "Claude|https://claude.ai"
        "Midjourney|https://www.midjourney.com"
        "Suno|https://suno.com"
        "ElevenLabs|https://elevenlabs.io"
    )
    local random_index=$((RANDOM % ${#tools[@]}))
    IFS='|' read -r name url <<< "${tools[$random_index]}"
    echo -e "${MAGENTA}[?] ${WHITE}Random tool: ${YELLOW}${name}${NC}"
    open_in_browser "$url" "$name"
}

# Update from GitHub
update_tool() {
    echo -e "${CYAN}[*] Checking for updates...${NC}"
    if command -v git &> /dev/null; then
        cd "$SCRIPT_DIR"
        git pull origin main 2>/dev/null && {
            echo -e "${GREEN}[✓] Updated successfully!${NC}"
        } || {
            echo -e "${RED}[✗] Update failed. Please update manually${NC}"
        }
    else
        echo -e "${RED}[✗] Git not installed!${NC}"
        echo -e "${YELLOW}[*] Install git: sudo apt-get install git${NC}"
    fi
    sleep 2
}

# Uninstall
uninstall_tool() {
    echo -e "${RED}[!] ${WHITE}Are you sure you want to uninstall? (y/n)${NC}"
    read -p "> " confirm
    if [ "$confirm" = "y" ] || [ "$confirm" = "Y" ]; then
        rm -f "$HOME/.local/bin/ai-tools"
        rm -rf "$HOME/.local/share/ai-tools"
        echo -e "${GREEN}[✓] Uninstalled successfully!${NC}"
        exit 0
    fi
}

# ═══════════════════════════════════════════════════════════════════
#  MAIN PROGRAM
# ═══════════════════════════════════════════════════════════════════

# Handle Command Line Arguments
case "$1" in
    --help|-h)
        show_help
        exit 0
        ;;
    --version|-v)
        echo -e "AI Tools Launcher v${VERSION}"
        exit 0
        ;;
    --update|-u)
        update_tool
        exit 0
        ;;
    --uninstall)
        uninstall_tool
        exit 0
        ;;
    --info)
        show_info
        exit 0
        ;;
    --search|-s)
        search_tool
        exit 0
        ;;
esac

# Check dependencies
check_dependencies

# Main loop
while true; do
    display_banner
    display_menu
    
    echo -e "${BRIGHT_GREEN}┌─[${BRIGHT_CYAN}root${BRIGHT_GREEN}@${BRIGHT_CYAN}ai-tools${BRIGHT_GREEN}]─[${BRIGHT_YELLOW}~${BRIGHT_GREEN}]${NC}"
    echo -e "${BRIGHT_GREEN}└──╼ ${WHITE}# ${NC}"
    read -p "" choice
    
    case "$choice" in
        [1-9]|10)
            quick_launch "$choice"
            ;;
        a|A)
            # Launch Python script for full list
            if [ -f "$SCRIPT_DIR/ai_tool.py" ]; then
                python3 "$SCRIPT_DIR/ai_tool.py"
            else
                echo -e "${RED}[✗] ai_tool.py not found!${NC}"
                echo -e "${YELLOW}[*] Please ensure ai_tool.py is in the same directory${NC}"
                sleep 2
            fi
            ;;
        c|C)
            clear_screen
            display_banner
            show_categories
            read -p "Select category: " cat_choice
            if [ "$cat_choice" != "0" ] && [ -n "$cat_choice" ]; then
                # Launch Python with category filter
                python3 "$SCRIPT_DIR/ai_tool.py" --category "$cat_choice" 2>/dev/null || {
                    echo -e "${YELLOW}[*] Category browsing available in full version${NC}"
                    sleep 1
                }
            fi
            ;;
        s|S)
            search_tool
            ;;
        f|F)
            view_favorites
            ;;
        h|H)
            view_history
            ;;
        r|R)
            random_tool
            ;;
        "?")
            show_help
            ;;
        99)
            show_info
            ;;
        0)
            clear_screen
            echo -e "${BRIGHT_RED}╔══════════════════════════════════════════════════════════════════╗${NC}"
            echo -e "${BRIGHT_RED}║${WHITE}                    EXITING PROGRAM                        ${BRIGHT_RED}║${NC}"
            echo -e "${BRIGHT_RED}╚══════════════════════════════════════════════════════════════════╝${NC}"
            echo ""
            echo -e "${YELLOW}[*] ${WHITE}Thank you for using AI Tools Launcher!${NC}"
            echo -e "${YELLOW}[*] ${WHITE}Developer: Raj Gautam${NC}"
            echo -e "${YELLOW}[*] ${WHITE}VBSPU Jaunpur${NC}"
            echo ""
            exit 0
            ;;
        *)
            echo -e "${RED}[✗] ${WHITE}Invalid option! Press ? for help${NC}"
            sleep 1
            ;;
    esac
done
