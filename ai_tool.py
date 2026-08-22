#!/usr/bin/env python3
"""
AI TOOLS LAUNCHER v3.0 - Ultimate Edition
Developer: Raj Gautam
BCA Student @ VBSPU, Jaunpur
Features: 120 AI Tools, Categories, Favorites, History, Search, Random Picker
"""

import os
import sys
import time
import webbrowser
import platform
import random
import json
from datetime import datetime

# ANSI Color Codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

# 120 AI Tools Database
AI_TOOLS = {
    1: {"name": "ChatGPT", "url": "https://chat.openai.com", "type": "Chat Assistant", "price": "Free/Paid", "desc": "OpenAI's flagship AI chatbot"},
    2: {"name": "DeepSeek AI", "url": "https://chat.deepseek.com", "type": "Chat Assistant", "price": "Free", "desc": "Advanced AI for coding and analysis"},
    3: {"name": "Claude AI", "url": "https://claude.ai", "type": "Chat Assistant", "price": "Free/Paid", "desc": "Anthropic's safe and capable AI"},
    4: {"name": "Google Gemini", "url": "https://gemini.google.com", "type": "Chat Assistant", "price": "Free/Paid", "desc": "Google's multimodal AI assistant"},
    5: {"name": "Microsoft Copilot", "url": "https://copilot.microsoft.com", "type": "Chat Assistant", "price": "Free/Paid", "desc": "AI assistant integrated with Microsoft"},
    6: {"name": "Meta AI", "url": "https://www.meta.ai", "type": "Chat Assistant", "price": "Free", "desc": "Meta's AI assistant"},
    7: {"name": "Character.AI", "url": "https://character.ai", "type": "Chat Assistant", "price": "Free/Paid", "desc": "Chat with AI characters"},
    8: {"name": "Poe", "url": "https://poe.com", "type": "Chat Assistant", "price": "Free/Paid", "desc": "Access multiple AI models"},
    9: {"name": "Pi AI", "url": "https://pi.ai", "type": "Chat Assistant", "price": "Free", "desc": "Personal AI by Inflection"},
    10: {"name": "Perplexity AI", "url": "https://www.perplexity.ai", "type": "Chat Assistant", "price": "Free/Paid", "desc": "AI-powered answer engine"},
    11: {"name": "You.com", "url": "https://you.com", "type": "Search Engine", "price": "Free/Paid", "desc": "AI-powered search engine"},
    12: {"name": "Phind", "url": "https://www.phind.com", "type": "Search Engine", "price": "Free", "desc": "AI search for developers"},
    13: {"name": "Andi Search", "url": "https://andisearch.com", "type": "Search Engine", "price": "Free", "desc": "AI search with visual answers"},
    14: {"name": "Brave Search AI", "url": "https://search.brave.com", "type": "Search Engine", "price": "Free", "desc": "Privacy-focused AI search"},
    15: {"name": "Komo Search", "url": "https://komo.ai", "type": "Search Engine", "price": "Free/Paid", "desc": "AI-powered search platform"},
    16: {"name": "Jasper AI", "url": "https://www.jasper.ai", "type": "Writing", "price": "Paid", "desc": "AI content creation platform"},
    17: {"name": "Copy.ai", "url": "https://www.copy.ai", "type": "Writing", "price": "Free/Paid", "desc": "AI copywriting assistant"},
    18: {"name": "Writesonic", "url": "https://writesonic.com", "type": "Writing", "price": "Free/Paid", "desc": "AI article and blog writer"},
    19: {"name": "Grammarly", "url": "https://www.grammarly.com", "type": "Writing", "price": "Free/Paid", "desc": "AI writing assistant"},
    20: {"name": "QuillBot", "url": "https://quillbot.com", "type": "Writing", "price": "Free/Paid", "desc": "AI paraphrasing tool"},
    21: {"name": "Rytr", "url": "https://rytr.me", "type": "Writing", "price": "Free/Paid", "desc": "AI writing assistant"},
    22: {"name": "Wordtune", "url": "https://www.wordtune.com", "type": "Writing", "price": "Free/Paid", "desc": "AI writing improvement"},
    23: {"name": "Sudowrite", "url": "https://www.sudowrite.com", "type": "Writing", "price": "Paid", "desc": "AI creative writing tool"},
    24: {"name": "NovelAI", "url": "https://novelai.net", "type": "Writing", "price": "Free/Paid", "desc": "AI storytelling assistant"},
    25: {"name": "Anyword", "url": "https://anyword.com", "type": "Writing", "price": "Paid", "desc": "AI marketing copy generator"},
    26: {"name": "Midjourney", "url": "https://www.midjourney.com", "type": "Image Generation", "price": "Paid", "desc": "Premium AI art generator"},
    27: {"name": "DALL-E 3", "url": "https://openai.com/dall-e-3", "type": "Image Generation", "price": "Paid", "desc": "OpenAI's image generator"},
    28: {"name": "Stable Diffusion", "url": "https://stability.ai", "type": "Image Generation", "price": "Free/Paid", "desc": "Open-source image generation"},
    29: {"name": "Leonardo AI", "url": "https://leonardo.ai", "type": "Image Generation", "price": "Free/Paid", "desc": "Creative AI image platform"},
    30: {"name": "Canva AI", "url": "https://www.canva.com", "type": "Image Generation", "price": "Free/Paid", "desc": "Design with AI features"},
    31: {"name": "Adobe Firefly", "url": "https://firefly.adobe.com", "type": "Image Generation", "price": "Free/Paid", "desc": "Adobe's AI image generator"},
    32: {"name": "Bing Image Creator", "url": "https://www.bing.com/create", "type": "Image Generation", "price": "Free", "desc": "Microsoft's image generator"},
    33: {"name": "Ideogram", "url": "https://ideogram.ai", "type": "Image Generation", "price": "Free/Paid", "desc": "AI text-to-image tool"},
    34: {"name": "Playground AI", "url": "https://playground.ai", "type": "Image Generation", "price": "Free/Paid", "desc": "AI image playground"},
    35: {"name": "DreamStudio", "url": "https://dreamstudio.ai", "type": "Image Generation", "price": "Free/Paid", "desc": "Stability AI's image tool"},
    36: {"name": "Runway ML", "url": "https://runwayml.com", "type": "Video Generation", "price": "Free/Paid", "desc": "AI video editing suite"},
    37: {"name": "Synthesia", "url": "https://www.synthesia.io", "type": "Video Generation", "price": "Paid", "desc": "AI video with avatars"},
    38: {"name": "Pika Labs", "url": "https://pika.art", "type": "Video Generation", "price": "Free/Paid", "desc": "AI video generation"},
    39: {"name": "HeyGen", "url": "https://www.heygen.com", "type": "Video Generation", "price": "Free/Paid", "desc": "AI video creation platform"},
    40: {"name": "Descript", "url": "https://www.descript.com", "type": "Video Editing", "price": "Free/Paid", "desc": "AI video and audio editing"},
    41: {"name": "InVideo AI", "url": "https://invideo.io", "type": "Video Generation", "price": "Free/Paid", "desc": "AI video creator"},
    42: {"name": "Pictory", "url": "https://pictory.ai", "type": "Video Generation", "price": "Free/Paid", "desc": "AI video from text"},
    43: {"name": "Lumen5", "url": "https://lumen5.com", "type": "Video Generation", "price": "Free/Paid", "desc": "AI video maker"},
    44: {"name": "Fliki", "url": "https://fliki.ai", "type": "Video Generation", "price": "Free/Paid", "desc": "AI text-to-video tool"},
    45: {"name": "CapCut AI", "url": "https://www.capcut.com", "type": "Video Editing", "price": "Free/Paid", "desc": "AI-powered video editor"},
    46: {"name": "ElevenLabs", "url": "https://elevenlabs.io", "type": "Voice Generation", "price": "Free/Paid", "desc": "AI voice synthesis"},
    47: {"name": "Murf AI", "url": "https://murf.ai", "type": "Voice Generation", "price": "Free/Paid", "desc": "AI text-to-speech"},
    48: {"name": "Suno AI", "url": "https://suno.com", "type": "Music Generation", "price": "Free/Paid", "desc": "AI music generator"},
    49: {"name": "AIVA", "url": "https://www.aiva.ai", "type": "Music Generation", "price": "Free/Paid", "desc": "AI music composer"},
    50: {"name": "Soundraw", "url": "https://soundraw.io", "type": "Music Generation", "price": "Free/Paid", "desc": "AI royalty-free music"},
    51: {"name": "Otter.ai", "url": "https://otter.ai", "type": "Transcription", "price": "Free/Paid", "desc": "AI meeting transcription"},
    52: {"name": "Whisper AI", "url": "https://openai.com/research/whisper", "type": "Transcription", "price": "Free", "desc": "OpenAI's speech recognition"},
    53: {"name": "Podcastle", "url": "https://podcastle.ai", "type": "Audio Editing", "price": "Free/Paid", "desc": "AI podcast editing"},
    54: {"name": "Adobe Podcast", "url": "https://podcast.adobe.com", "type": "Audio Editing", "price": "Free/Paid", "desc": "AI audio enhancement"},
    55: {"name": "Krisp", "url": "https://krisp.ai", "type": "Audio Enhancement", "price": "Free/Paid", "desc": "AI noise cancellation"},
    56: {"name": "GitHub Copilot", "url": "https://github.com/features/copilot", "type": "Code Assistant", "price": "Paid", "desc": "AI pair programmer"},
    57: {"name": "Codeium", "url": "https://codeium.com", "type": "Code Assistant", "price": "Free/Paid", "desc": "Free AI code completion"},
    58: {"name": "Tabnine", "url": "https://www.tabnine.com", "type": "Code Assistant", "price": "Free/Paid", "desc": "AI code completion"},
    59: {"name": "Replit AI", "url": "https://replit.com", "type": "Code Assistant", "price": "Free/Paid", "desc": "AI-powered coding platform"},
    60: {"name": "Cursor", "url": "https://cursor.sh", "type": "Code Assistant", "price": "Free/Paid", "desc": "AI-first code editor"},
    61: {"name": "CodeWhisperer", "url": "https://aws.amazon.com/codewhisperer", "type": "Code Assistant", "price": "Free/Paid", "desc": "Amazon's AI code tool"},
    62: {"name": "Sourcegraph Cody", "url": "https://sourcegraph.com/cody", "type": "Code Assistant", "price": "Free/Paid", "desc": "AI code understanding"},
    63: {"name": "Mutable AI", "url": "https://mutable.ai", "type": "Code Assistant", "price": "Free/Paid", "desc": "AI code generation"},
    64: {"name": "Bito AI", "url": "https://bito.ai", "type": "Code Assistant", "price": "Free/Paid", "desc": "AI code review"},
    65: {"name": "Snyk Code", "url": "https://snyk.io", "type": "Code Security", "price": "Free/Paid", "desc": "AI security scanning"},
    66: {"name": "DeepCode", "url": "https://www.deepcode.ai", "type": "Code Review", "price": "Free/Paid", "desc": "AI code analysis"},
    67: {"name": "CodeGeeX", "url": "https://codegeex.cn", "type": "Code Assistant", "price": "Free", "desc": "Free AI code generator"},
    68: {"name": "AskCodi", "url": "https://www.askcodi.com", "type": "Code Assistant", "price": "Free/Paid", "desc": "AI coding assistant"},
    69: {"name": "Blackbox AI", "url": "https://www.blackbox.ai", "type": "Code Assistant", "price": "Free/Paid", "desc": "AI code search"},
    70: {"name": "Warp AI", "url": "https://www.warp.dev", "type": "Terminal AI", "price": "Free/Paid", "desc": "AI-powered terminal"},
    71: {"name": "Hugging Face", "url": "https://huggingface.co", "type": "Development", "price": "Free/Paid", "desc": "AI models platform"},
    72: {"name": "Replicate", "url": "https://replicate.com", "type": "Development", "price": "Free/Paid", "desc": "Cloud AI models"},
    73: {"name": "OpenAI API", "url": "https://platform.openai.com", "type": "Development", "price": "Paid", "desc": "GPT API access"},
    74: {"name": "Anthropic API", "url": "https://console.anthropic.com", "type": "Development", "price": "Paid", "desc": "Claude API access"},
    75: {"name": "Google AI Studio", "url": "https://aistudio.google.com", "type": "Development", "price": "Free/Paid", "desc": "Gemini API platform"},
    76: {"name": "Cohere", "url": "https://cohere.com", "type": "Development", "price": "Free/Paid", "desc": "NLP API platform"},
    77: {"name": "AI21 Labs", "url": "https://www.ai21.com", "type": "Development", "price": "Free/Paid", "desc": "Jurassic models"},
    78: {"name": "Together AI", "url": "https://www.together.ai", "type": "Development", "price": "Free/Paid", "desc": "Open-source AI cloud"},
    79: {"name": "Modal", "url": "https://modal.com", "type": "Development", "price": "Free/Paid", "desc": "Serverless AI compute"},
    80: {"name": "LangChain", "url": "https://www.langchain.com", "type": "Development", "price": "Free/Paid", "desc": "AI app framework"},
    81: {"name": "Notion AI", "url": "https://www.notion.so", "type": "Productivity", "price": "Free/Paid", "desc": "AI workspace assistant"},
    82: {"name": "Mem", "url": "https://get.mem.ai", "type": "Productivity", "price": "Free/Paid", "desc": "AI note-taking"},
    83: {"name": "Taskade AI", "url": "https://www.taskade.com", "type": "Productivity", "price": "Free/Paid", "desc": "AI task management"},
    84: {"name": "Motion", "url": "https://www.usemotion.com", "type": "Productivity", "price": "Paid", "desc": "AI calendar assistant"},
    85: {"name": "Reclaim AI", "url": "https://reclaim.ai", "type": "Productivity", "price": "Free/Paid", "desc": "AI schedule optimizer"},
    86: {"name": "Fireflies.ai", "url": "https://fireflies.ai", "type": "Productivity", "price": "Free/Paid", "desc": "AI meeting assistant"},
    87: {"name": "Beautiful.ai", "url": "https://www.beautiful.ai", "type": "Presentations", "price": "Free/Paid", "desc": "AI presentation maker"},
    88: {"name": "Tome", "url": "https://tome.app", "type": "Presentations", "price": "Free/Paid", "desc": "AI storytelling tool"},
    89: {"name": "Gamma", "url": "https://gamma.app", "type": "Presentations", "price": "Free/Paid", "desc": "AI presentation generator"},
    90: {"name": "Slides AI", "url": "https://www.slidesai.io", "type": "Presentations", "price": "Free/Paid", "desc": "AI Google Slides tool"},
    91: {"name": "Mixo", "url": "https://www.mixo.io", "type": "Website Builder", "price": "Free/Paid", "desc": "AI website generator"},
    92: {"name": "Framer AI", "url": "https://www.framer.com", "type": "Website Builder", "price": "Free/Paid", "desc": "AI web design tool"},
    93: {"name": "Browse AI", "url": "https://www.browse.ai", "type": "Automation", "price": "Free/Paid", "desc": "AI web scraping"},
    94: {"name": "Zapier AI", "url": "https://zapier.com", "type": "Automation", "price": "Free/Paid", "desc": "AI workflow automation"},
    95: {"name": "Lindy AI", "url": "https://www.lindy.ai", "type": "Assistant", "price": "Free/Paid", "desc": "AI personal assistant"},
    96: {"name": "AgentGPT", "url": "https://agentgpt.reworkd.ai", "type": "Autonomous AI", "price": "Free/Paid", "desc": "Autonomous AI agents"},
    97: {"name": "AutoGPT", "url": "https://autogpt.net", "type": "Autonomous AI", "price": "Free", "desc": "Autonomous AI framework"},
    98: {"name": "BabyAGI", "url": "https://babyagi.org", "type": "Autonomous AI", "price": "Free", "desc": "Task-driven AI"},
    99: {"name": "Gradio", "url": "https://www.gradio.app", "type": "Development", "price": "Free", "desc": "ML web apps"},
    100: {"name": "Streamlit", "url": "https://streamlit.io", "type": "Development", "price": "Free", "desc": "AI app builder"},
    # Additional 20 tools
    101: {"name": "Copy.ai", "url": "https://www.copy.ai", "type": "Writing", "price": "Free/Paid", "desc": "AI copywriting assistant"},
    102: {"name": "Writesonic", "url": "https://writesonic.com", "type": "Writing", "price": "Free/Paid", "desc": "AI article and blog writer"},
    103: {"name": "QuillBot", "url": "https://quillbot.com", "type": "Writing", "price": "Free/Paid", "desc": "AI paraphrasing tool"},
    104: {"name": "Rytr", "url": "https://rytr.me", "type": "Writing", "price": "Free/Paid", "desc": "AI writing assistant"},
    105: {"name": "Wordtune", "url": "https://www.wordtune.com", "type": "Writing", "price": "Free/Paid", "desc": "AI writing improvement"},
    106: {"name": "Sudowrite", "url": "https://www.sudowrite.com", "type": "Writing", "price": "Paid", "desc": "AI creative writing tool"},
    107: {"name": "NovelAI", "url": "https://novelai.net", "type": "Writing", "price": "Free/Paid", "desc": "AI storytelling assistant"},
    108: {"name": "Anyword", "url": "https://anyword.com", "type": "Writing", "price": "Paid", "desc": "AI marketing copy generator"},
    109: {"name": "CopySmith", "url": "https://copysmith.ai", "type": "Writing", "price": "Paid", "desc": "AI eCommerce copywriter"},
    110: {"name": "Frase", "url": "https://www.frase.io", "type": "Writing", "price": "Paid", "desc": "AI SEO content tool"},
    111: {"name": "Surfer SEO", "url": "https://surferseo.com", "type": "Writing", "price": "Paid", "desc": "AI content optimization"},
    112: {"name": "MarketMuse", "url": "https://www.marketmuse.com", "type": "Writing", "price": "Paid", "desc": "AI content planning"},
    113: {"name": "Clearscope", "url": "https://www.clearscope.io", "type": "Writing", "price": "Paid", "desc": "AI content optimization"},
    114: {"name": "INK Editor", "url": "https://inkforall.com", "type": "Writing", "price": "Free/Paid", "desc": "AI SEO writing assistant"},
    115: {"name": "Outranking", "url": "https://www.outranking.io", "type": "Writing", "price": "Paid", "desc": "AI content strategy"},
    116: {"name": "Scalenut", "url": "https://www.scalenut.com", "type": "Writing", "price": "Paid", "desc": "AI content creation"},
    117: {"name": "ContentBot", "url": "https://contentbot.ai", "type": "Writing", "price": "Free/Paid", "desc": "AI content automation"},
    118: {"name": "Peppertype", "url": "https://www.peppertype.ai", "type": "Writing", "price": "Paid", "desc": "AI content generator"},
    119: {"name": "Copyscape", "url": "https://www.copyscape.com", "type": "Writing", "price": "Paid", "desc": "Plagiarism checker"},
    120: {"name": "Hemingway Editor", "url": "https://hemingwayapp.com", "type": "Writing", "price": "Free/Paid", "desc": "AI writing style editor"},
}

# Category mapping
CATEGORIES = {}
for tid, tool in AI_TOOLS.items():
    cat = tool['type']
    if cat not in CATEGORIES:
        CATEGORIES[cat] = []
    CATEGORIES[cat].append(tid)

# Global state
favorites = set()  # set of tool IDs
history = []       # list of opened tool IDs (most recent first)

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def loading_animation(duration=1.0, message="LOADING"):
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        frame = frames[i % len(frames)]
        progress = int((1 - (end_time - time.time()) / duration) * 20)
        bar = '█' * progress + '░' * (20 - progress)
        sys.stdout.write(f'\r{Colors.CYAN}[{frame}] {Colors.BRIGHT_WHITE}{message} {Colors.BRIGHT_GREEN}{bar} {Colors.BRIGHT_YELLOW}{progress*5}%{Colors.RESET}')
        sys.stdout.flush()
        time.sleep(0.05)
        i += 1
    sys.stdout.write('\r' + ' ' * 60 + '\r')

def matrix_effect(duration=0.8):
    end_time = time.time() + duration
    matrix_chars = "01ABCDEF"
    colors = [Colors.BRIGHT_GREEN, Colors.GREEN, Colors.BRIGHT_CYAN]
    while time.time() < end_time:
        for _ in range(2):
            line = ''
            for _ in range(30):
                char = random.choice(matrix_chars)
                color = random.choice(colors)
                line += f'{color}{char} {Colors.RESET}'
            print(f'\r{line}', end='', flush=True)
            time.sleep(0.02)
    print('\r' + ' ' * 60 + '\r')

def display_banner():
    logo = f"""
{Colors.BRIGHT_RED}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════╗
{Colors.BRIGHT_RED}║{Colors.BRIGHT_CYAN}  █████╗ ██╗    ████████╗ ██████╗  ██████╗ ██╗          {Colors.BRIGHT_RED}║
{Colors.BRIGHT_RED}║{Colors.BRIGHT_CYAN} ██╔══██╗██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║          {Colors.BRIGHT_RED}║
{Colors.BRIGHT_RED}║{Colors.BRIGHT_CYAN} ███████║██║       ██║   ██║   ██║██║   ██║██║          {Colors.BRIGHT_RED}║
{Colors.BRIGHT_RED}║{Colors.BRIGHT_CYAN} ██╔══██║██║       ██║   ██║   ██║██║   ██║██║          {Colors.BRIGHT_RED}║
{Colors.BRIGHT_RED}║{Colors.BRIGHT_CYAN} ██║  ██║███████╗  ██║   ╚██████╔╝╚██████╔╝███████╗     {Colors.BRIGHT_RED}║
{Colors.BRIGHT_RED}║{Colors.BRIGHT_CYAN} ╚═╝  ╚═╝╚══════╝  ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝     {Colors.BRIGHT_RED}║
{Colors.BRIGHT_RED}╠══════════════════════════════════════════════════════════════════╣
{Colors.BRIGHT_RED}║{Colors.BRIGHT_WHITE}       120+ AI TOOLS LAUNCHER v3.0 - ULTIMATE EDITION         {Colors.BRIGHT_RED}║
{Colors.BRIGHT_RED}║{Colors.BRIGHT_YELLOW}       ⚡ Powered by Raj Gautam | VBSPU Jaunpur ⚡             {Colors.BRIGHT_RED}║
{Colors.BRIGHT_RED}╚══════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(logo)
    
    # System stats
    total = len(AI_TOOLS)
    free = sum(1 for t in AI_TOOLS.values() if "Free" in t['price'])
    paid = total - free
    print(f"{Colors.BRIGHT_GREEN}[✓] {Colors.BRIGHT_WHITE}Total Tools: {Colors.BRIGHT_YELLOW}{total} {Colors.DIM}| {Colors.BRIGHT_WHITE}Free: {Colors.BRIGHT_GREEN}{free} {Colors.DIM}| {Colors.BRIGHT_WHITE}Paid: {Colors.BRIGHT_RED}{paid}{Colors.RESET}")
    print(f"{Colors.BRIGHT_GREEN}[✓] {Colors.BRIGHT_WHITE}Favorites: {Colors.BRIGHT_MAGENTA}{len(favorites)}{Colors.RESET} {Colors.DIM}| {Colors.BRIGHT_WHITE}History: {Colors.BRIGHT_CYAN}{len(history)}{Colors.RESET}")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{Colors.BRIGHT_GREEN}[✓] {Colors.BRIGHT_WHITE}System Time: {Colors.BRIGHT_BLUE}{now}{Colors.RESET}\n")

def display_info():
    clear_screen()
    info = f"""
{Colors.BRIGHT_CYAN}╔══════════════════════════════════════════════════════════════════╗
{Colors.BRIGHT_CYAN}║{Colors.BRIGHT_WHITE}{Colors.BOLD}                    DEVELOPER INFORMATION                      {Colors.RESET}{Colors.BRIGHT_CYAN}║
{Colors.BRIGHT_CYAN}╠══════════════════════════════════════════════════════════════════╣
{Colors.BRIGHT_CYAN}║ {Colors.BRIGHT_GREEN}Name:{Colors.RESET}        Raj Gautam                                  {Colors.BRIGHT_CYAN}║
{Colors.BRIGHT_CYAN}║ {Colors.BRIGHT_GREEN}Education:{Colors.RESET}    BCA Student                                 {Colors.BRIGHT_CYAN}║
{Colors.BRIGHT_CYAN}║ {Colors.BRIGHT_GREEN}University:{Colors.RESET}   VBSPU, Jaunpur                              {Colors.BRIGHT_CYAN}║
{Colors.BRIGHT_CYAN}║ {Colors.BRIGHT_GREEN}Interests:{Colors.RESET}    Software Dev, Cybersecurity, AI              {Colors.BRIGHT_CYAN}║
{Colors.BRIGHT_CYAN}║ {Colors.BRIGHT_GREEN}Motto:{Colors.RESET}       "Learn. Build. Experiment. Improve."        {Colors.BRIGHT_CYAN}║
{Colors.BRIGHT_CYAN}╠══════════════════════════════════════════════════════════════════╣
{Colors.BRIGHT_CYAN}║ {Colors.BRIGHT_YELLOW}Core Skills:                                                        {Colors.BRIGHT_CYAN}║
{Colors.BRIGHT_CYAN}║ {Colors.BRIGHT_WHITE}• Python Programming         • Web Development                {Colors.BRIGHT_CYAN}║
{Colors.BRIGHT_CYAN}║ {Colors.BRIGHT_WHITE}• Cybersecurity              • AI & Machine Learning          {Colors.BRIGHT_CYAN}║
{Colors.BRIGHT_CYAN}║ {Colors.BRIGHT_WHITE}• Linux Systems              • Database Management           {Colors.BRIGHT_CYAN}║
{Colors.BRIGHT_CYAN}╚══════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(info)

def display_categories():
    """Show categories with numbers"""
    print(f"\n{Colors.BRIGHT_YELLOW}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}{Colors.BOLD}║                       AI TOOL CATEGORIES                        ║{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}{Colors.BOLD}╚══════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    cat_list = sorted(CATEGORIES.keys())
    for i, cat in enumerate(cat_list, 1):
        count = len(CATEGORIES[cat])
        print(f"{Colors.BRIGHT_GREEN}[{i:2d}]{Colors.RESET} {Colors.BRIGHT_CYAN}{cat:<25}{Colors.RESET} {Colors.BRIGHT_WHITE}({count} tools){Colors.RESET}")
    print(f"\n{Colors.BRIGHT_YELLOW}[0] {Colors.BRIGHT_WHITE}Back to Main Menu{Colors.RESET}")

def display_menu(page=1, category=None):
    """Display tools, optionally filtered by category"""
    items_per_page = 20
    if category:
        # Filter tool IDs by category
        tool_ids = CATEGORIES.get(category, [])
        total_pages = (len(tool_ids) + items_per_page - 1) // items_per_page
        start_idx = (page - 1) * items_per_page
        end_idx = min(start_idx + items_per_page, len(tool_ids))
        page_ids = tool_ids[start_idx:end_idx]
        header = f"AI TOOLS - {category} (Page {page}/{total_pages})"
    else:
        total_pages = (len(AI_TOOLS) + items_per_page - 1) // items_per_page
        start_idx = (page - 1) * items_per_page + 1
        end_idx = min(start_idx + items_per_page - 1, len(AI_TOOLS))
        page_ids = list(range(start_idx, end_idx + 1))
        header = f"AI TOOLS DATABASE - PAGE {page}/{total_pages}"
    
    print(f"\n{Colors.BRIGHT_YELLOW}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}{Colors.BOLD}║ {header:<64} ║{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}{Colors.BOLD}╚══════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    print(f"{Colors.BRIGHT_CYAN}{'─'*70}{Colors.RESET}")
    print(f"{Colors.BRIGHT_WHITE}{'ID':<5} {'Tool Name':<25} {'Type':<20} {'Price':<10}{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{'─'*70}{Colors.RESET}")
    
    for tid in page_ids:
        if tid in AI_TOOLS:
            tool = AI_TOOLS[tid]
            price_color = Colors.BRIGHT_GREEN if "Free" in tool['price'] else Colors.BRIGHT_RED
            fav_mark = "♥" if tid in favorites else " "
            print(f"{Colors.BRIGHT_GREEN}[{tid:3d}]{Colors.RESET}{fav_mark} {Colors.BRIGHT_CYAN}{tool['name']:<24}{Colors.RESET} {Colors.BRIGHT_WHITE}{tool['type']:<19}{Colors.RESET} {price_color}{tool['price']:<10}{Colors.RESET}")
    
    print(f"{Colors.BRIGHT_CYAN}{'─'*70}{Colors.RESET}")
    
    # Navigation
    print(f"\n{Colors.BRIGHT_YELLOW}Navigation:{Colors.RESET}")
    if page > 1:
        print(f"{Colors.BRIGHT_CYAN}[P]{Colors.RESET} Prev", end="  ")
    if page < total_pages:
        print(f"{Colors.BRIGHT_CYAN}[N]{Colors.RESET} Next", end="  ")
    print(f"{Colors.BRIGHT_CYAN}[C]{Colors.RESET} Categories", end="  ")
    print(f"{Colors.BRIGHT_CYAN}[S]{Colors.RESET} Search", end="  ")
    print(f"{Colors.BRIGHT_CYAN}[F]{Colors.RESET} Favorites", end="  ")
    print(f"{Colors.BRIGHT_CYAN}[H]{Colors.RESET} History", end="  ")
    print(f"{Colors.BRIGHT_CYAN}[R]{Colors.RESET} Random", end="  ")
    print(f"{Colors.BRIGHT_CYAN}[?]{Colors.RESET} Help", end="  ")
    print(f"{Colors.BRIGHT_CYAN}[0]{Colors.RESET} Exit", end="  ")
    print(f"{Colors.BRIGHT_CYAN}[99]{Colors.RESET} Info")

def search_tools():
    print(f"\n{Colors.BRIGHT_YELLOW}[*] {Colors.BRIGHT_WHITE}Enter search term (or 'back'):{Colors.RESET}")
    term = input(f"{Colors.BRIGHT_GREEN}└──╼ {Colors.BRIGHT_WHITE}# {Colors.RESET}").strip().lower()
    if term == 'back':
        return
    results = []
    for tid, tool in AI_TOOLS.items():
        if (term in tool['name'].lower() or term in tool['type'].lower() or term in tool['desc'].lower()):
            results.append(tid)
    if results:
        print(f"\n{Colors.BRIGHT_GREEN}[✓] {Colors.BRIGHT_WHITE}Found {len(results)} results:{Colors.RESET}\n")
        print(f"{Colors.BRIGHT_CYAN}{'─'*70}{Colors.RESET}")
        for tid in results[:10]:
            tool = AI_TOOLS[tid]
            price_color = Colors.BRIGHT_GREEN if "Free" in tool['price'] else Colors.BRIGHT_RED
            fav_mark = "♥" if tid in favorites else " "
            print(f"{Colors.BRIGHT_GREEN}[{tid:3d}]{Colors.RESET}{fav_mark} {Colors.BRIGHT_CYAN}{tool['name']:<25}{Colors.RESET} {Colors.BRIGHT_WHITE}{tool['type']:<20}{Colors.RESET} {price_color}{tool['price']}{Colors.RESET}")
            print(f"{Colors.RESET}      {Colors.DIM}{tool['desc']}{Colors.RESET}")
        print(f"{Colors.BRIGHT_CYAN}{'─'*70}{Colors.RESET}")
        print(f"\n{Colors.BRIGHT_YELLOW}Enter ID to open, or press Enter to return.{Colors.RESET}")
        choice = input(f"{Colors.BRIGHT_GREEN}└──╼ {Colors.BRIGHT_WHITE}# {Colors.RESET}").strip()
        if choice.isdigit():
            open_tool(int(choice))
    else:
        print(f"{Colors.BRIGHT_RED}[✗] {Colors.BRIGHT_WHITE}No results found for '{term}'{Colors.RESET}")
        time.sleep(1)

def show_favorites():
    if not favorites:
        print(f"\n{Colors.BRIGHT_YELLOW}[!] {Colors.BRIGHT_WHITE}No favorites yet. Mark tools by pressing F while viewing a tool, or use 'F' to toggle after selecting ID.{Colors.RESET}")
        time.sleep(1)
        return
    print(f"\n{Colors.BRIGHT_MAGENTA}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.BRIGHT_MAGENTA}{Colors.BOLD}║                         YOUR FAVORITES                          ║{Colors.RESET}")
    print(f"{Colors.BRIGHT_MAGENTA}{Colors.BOLD}╚══════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    print(f"{Colors.BRIGHT_CYAN}{'─'*70}{Colors.RESET}")
    print(f"{Colors.BRIGHT_WHITE}{'ID':<5} {'Tool Name':<25} {'Type':<20} {'Price':<10}{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{'─'*70}{Colors.RESET}")
    for tid in sorted(favorites):
        tool = AI_TOOLS[tid]
        price_color = Colors.BRIGHT_GREEN if "Free" in tool['price'] else Colors.BRIGHT_RED
        print(f"{Colors.BRIGHT_GREEN}[{tid:3d}]{Colors.RESET} {Colors.BRIGHT_CYAN}{tool['name']:<24}{Colors.RESET} {Colors.BRIGHT_WHITE}{tool['type']:<19}{Colors.RESET} {price_color}{tool['price']:<10}{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{'─'*70}{Colors.RESET}")
    print(f"\n{Colors.BRIGHT_YELLOW}Enter ID to open, or press Enter to return.{Colors.RESET}")
    choice = input(f"{Colors.BRIGHT_GREEN}└──╼ {Colors.BRIGHT_WHITE}# {Colors.RESET}").strip()
    if choice.isdigit():
        open_tool(int(choice))

def show_history():
    if not history:
        print(f"\n{Colors.BRIGHT_YELLOW}[!] {Colors.BRIGHT_WHITE}No history yet.{Colors.RESET}")
        time.sleep(1)
        return
    print(f"\n{Colors.BRIGHT_CYAN}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}║                         RECENT HISTORY                          ║{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}╚══════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    print(f"{Colors.BRIGHT_CYAN}{'─'*70}{Colors.RESET}")
    for idx, tid in enumerate(history[:10], 1):
        tool = AI_TOOLS[tid]
        print(f"{Colors.BRIGHT_WHITE}{idx}. {Colors.BRIGHT_CYAN}{tool['name']}{Colors.RESET} ({Colors.BRIGHT_YELLOW}{tool['type']}{Colors.RESET})")
    print(f"{Colors.BRIGHT_CYAN}{'─'*70}{Colors.RESET}")
    print(f"\n{Colors.BRIGHT_YELLOW}Enter number to re-open, or press Enter to return.{Colors.RESET}")
    choice = input(f"{Colors.BRIGHT_GREEN}└──╼ {Colors.BRIGHT_WHITE}# {Colors.RESET}").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(history[:10]):
        open_tool(history[int(choice)-1])

def toggle_favorite(tool_id):
    if tool_id in favorites:
        favorites.remove(tool_id)
        print(f"{Colors.BRIGHT_YELLOW}[♥] {Colors.BRIGHT_WHITE}Removed from favorites{Colors.RESET}")
    else:
        favorites.add(tool_id)
        print(f"{Colors.BRIGHT_RED}[♥] {Colors.BRIGHT_WHITE}Added to favorites{Colors.RESET}")
    time.sleep(0.8)

def random_tool():
    tid = random.choice(list(AI_TOOLS.keys()))
    print(f"\n{Colors.BRIGHT_MAGENTA}[?] {Colors.BRIGHT_WHITE}Random tool selected: {Colors.BRIGHT_YELLOW}{AI_TOOLS[tid]['name']}{Colors.RESET}")
    open_tool(tid)

def open_tool(tool_id):
    if tool_id not in AI_TOOLS:
        print(f"{Colors.BRIGHT_RED}[✗] {Colors.BRIGHT_WHITE}Invalid tool ID!{Colors.RESET}")
        time.sleep(1)
        return
    tool = AI_TOOLS[tool_id]
    
    # Add to history (avoid duplicates at top)
    if tool_id in history:
        history.remove(tool_id)
    history.insert(0, tool_id)
    
    print(f"\n{Colors.BRIGHT_CYAN}{'='*70}{Colors.RESET}")
    print(f"{Colors.BRIGHT_GREEN}⟳ ACCESSING: {tool['name']}{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{'='*70}{Colors.RESET}")
    print(f"{Colors.BRIGHT_WHITE}Type: {Colors.BRIGHT_YELLOW}{tool['type']}{Colors.RESET}")
    print(f"{Colors.BRIGHT_WHITE}Description: {Colors.BRIGHT_MAGENTA}{tool['desc']}{Colors.RESET}")
    print(f"{Colors.BRIGHT_WHITE}Price: {Colors.BRIGHT_GREEN if 'Free' in tool['price'] else Colors.BRIGHT_RED}{tool['price']}{Colors.RESET}")
    print(f"{Colors.BRIGHT_WHITE}URL: {Colors.BRIGHT_BLUE}{tool['url']}{Colors.RESET}")
    print(f"{Colors.BRIGHT_CYAN}{'='*70}{Colors.RESET}\n")
    
    # Ask if user wants to add to favorites
    fav_choice = input(f"{Colors.BRIGHT_MAGENTA}Add to favorites? (y/n): {Colors.RESET}").strip().lower()
    if fav_choice == 'y':
        toggle_favorite(tool_id)
    
    print(f"\n{Colors.BRIGHT_RED}[!] {Colors.BRIGHT_YELLOW}ESTABLISHING CONNECTION...{Colors.RESET}")
    loading_animation(1.0, "CONNECTING")
    
    print(f"{Colors.BRIGHT_GREEN}[✓] {Colors.BRIGHT_WHITE}Connection established!{Colors.RESET}")
    print(f"{Colors.BRIGHT_GREEN}[✓] {Colors.BRIGHT_WHITE}Bypassing security protocols...{Colors.RESET}")
    loading_animation(0.8, "BYPASSING")
    
    print(f"{Colors.BRIGHT_GREEN}[✓] {Colors.BRIGHT_WHITE}Opening {tool['name']} in browser...{Colors.RESET}\n")
    time.sleep(0.5)
    webbrowser.open(tool['url'])
    
    print(f"{Colors.BRIGHT_GREEN}[✓] {Colors.BRIGHT_WHITE}Success! {tool['name']} launched.{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}[*] {Colors.BRIGHT_WHITE}Returning to main menu...{Colors.RESET}")
    time.sleep(1.5)

def show_help():
    print(f"""
{Colors.BRIGHT_CYAN}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════╗
{Colors.BRIGHT_CYAN}{Colors.BOLD}║                         HELP & COMMANDS                         ║
{Colors.BRIGHT_CYAN}{Colors.BOLD}╚══════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.BRIGHT_YELLOW}Basic Navigation:{Colors.RESET}
  {Colors.BRIGHT_GREEN}[1-120]{Colors.RESET}  Open tool by ID
  {Colors.BRIGHT_GREEN}[N]{Colors.RESET}      Next page
  {Colors.BRIGHT_GREEN}[P]{Colors.RESET}      Previous page
  {Colors.BRIGHT_GREEN}[C]{Colors.RESET}      Browse by category
  {Colors.BRIGHT_GREEN}[S]{Colors.RESET}      Search tools
  {Colors.BRIGHT_GREEN}[F]{Colors.RESET}      View favorites
  {Colors.BRIGHT_GREEN}[H]{Colors.RESET}      View history
  {Colors.BRIGHT_GREEN}[R]{Colors.RESET}      Random tool
  {Colors.BRIGHT_GREEN}[?]{Colors.RESET}      Show this help
  {Colors.BRIGHT_GREEN}[99]{Colors.RESET}     Developer info
  {Colors.BRIGHT_GREEN}[0]{Colors.RESET}      Exit program

{Colors.BRIGHT_YELLOW}Tips:{Colors.RESET}
  • While viewing a tool, you can add it to favorites by pressing 'y'.
  • Favorites are shown with a {Colors.BRIGHT_RED}♥{Colors.RESET} symbol.
  • History stores your 10 most recent tools.
  • Categories allow you to filter by tool type.
""")
    input(f"\n{Colors.BRIGHT_GREEN}Press Enter to continue...{Colors.RESET}")

def main():
    current_page = 1
    current_category = None
    
    while True:
        clear_screen()
        matrix_effect(0.5)
        display_banner()
        if current_category:
            display_menu(current_page, current_category)
        else:
            display_menu(current_page)
        
        try:
            choice = input(f"\n{Colors.BRIGHT_GREEN}┌─[{Colors.BRIGHT_CYAN}root{Colors.BRIGHT_GREEN}@{Colors.BRIGHT_CYAN}ai-tools{Colors.BRIGHT_GREEN}]─[{Colors.BRIGHT_YELLOW}~{Colors.BRIGHT_GREEN}]\n{Colors.BRIGHT_GREEN}└──╼ {Colors.BRIGHT_WHITE}# {Colors.RESET}").strip().lower()
            
            if choice == '':
                continue
            elif choice == 'p':
                if current_page > 1:
                    current_page -= 1
            elif choice == 'n':
                if current_category:
                    total = len(CATEGORIES.get(current_category, []))
                    if current_page * 20 < total:
                        current_page += 1
                else:
                    if current_page < 6:  # 120/20 = 6 pages
                        current_page += 1
            elif choice == 'c':
                # Show categories
                while True:
                    clear_screen()
                    display_banner()
                    display_categories()
                    cat_choice = input(f"\n{Colors.BRIGHT_GREEN}Select category number (0 to back): {Colors.RESET}").strip()
                    if cat_choice == '0':
                        break
                    if cat_choice.isdigit():
                        idx = int(cat_choice) - 1
                        cat_list = sorted(CATEGORIES.keys())
                        if 0 <= idx < len(cat_list):
                            current_category = cat_list[idx]
                            current_page = 1
                            break
                        else:
                            print(f"{Colors.BRIGHT_RED}Invalid category.{Colors.RESET}")
                            time.sleep(0.5)
            elif choice == 's':
                search_tools()
            elif choice == 'f':
                show_favorites()
            elif choice == 'h':
                show_history()
            elif choice == 'r':
                random_tool()
            elif choice == '?':
                show_help()
            elif choice == '0':
                print(f"\n{Colors.BRIGHT_RED}╔══════════════════════════════════════════════════════════════════╗")
                print(f"{Colors.BRIGHT_RED}║{Colors.BRIGHT_WHITE}                    EXITING PROGRAM                        {Colors.BRIGHT_RED}║")
                print(f"{Colors.BRIGHT_RED}╚══════════════════════════════════════════════════════════════════╝{Colors.RESET}")
                print(f"{Colors.BRIGHT_YELLOW}[*] {Colors.BRIGHT_WHITE}Thank you for using AI Tools Launcher!{Colors.RESET}")
                print(f"{Colors.BRIGHT_YELLOW}[*] {Colors.BRIGHT_WHITE}Developer: Raj Gautam{Colors.RESET}")
                print(f"{Colors.BRIGHT_YELLOW}[*] {Colors.BRIGHT_WHITE}VBSPU Jaunpur{Colors.RESET}\n")
                sys.exit(0)
            elif choice == '99':
                display_info()
                input(f"\n{Colors.BRIGHT_GREEN}Press Enter to return...{Colors.RESET}")
            elif choice.isdigit():
                tool_id = int(choice)
                if 1 <= tool_id <= len(AI_TOOLS):
                    open_tool(tool_id)
                else:
                    print(f"{Colors.BRIGHT_RED}[✗] {Colors.BRIGHT_WHITE}Invalid ID. Use 1-{len(AI_TOOLS)}.{Colors.RESET}")
                    time.sleep(0.8)
            else:
                print(f"{Colors.BRIGHT_RED}[✗] {Colors.BRIGHT_WHITE}Unknown command. Press ? for help.{Colors.RESET}")
                time.sleep(0.8)
        except KeyboardInterrupt:
            print(f"\n\n{Colors.BRIGHT_RED}[!] {Colors.BRIGHT_YELLOW}Operation cancelled. Exiting...{Colors.RESET}")
            sys.exit(0)
        except Exception as e:
            print(f"{Colors.BRIGHT_RED}[✗] {Colors.BRIGHT_WHITE}Error: {e}{Colors.RESET}")
            time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.BRIGHT_RED}[!] {Colors.BRIGHT_YELLOW}Program terminated.{Colors.RESET}")
        sys.exit(0)
