# Mochi AI Discord Bot 🐾

A cute little Discord bot with a built-in AI personality (based on ChatGPT), made by **justdev-chris** 💖. Uses OpenRouter's Cypher-Alpha free model and can be easily hosted on Replit or Railway.

---

## ✨ Features

- AI personality with cuddly, nerdy, sleepy catboy vibes  
- Able to DM the bot
- Supports message replies using the Cypher-Alpha free model  
- Simple setup, fully self-contained bot  

---

## 💾 Requirements

- Python 3.10 or later  
- `discord.py`  
- `aiohttp`  
- `requests`  
- `python-dotenv`  

You can install all required packages using:

pip install -r requirements.txt

---

## 📦 Installation

### 🧪 Method 1: Clone via Git

git clone https://github.com/justdev-chris/Mochi-AI-DISCORD.git
cd Mochi-AI-DISCORD-main
pip install -r requirements.txt

### 📁 Method 2: Manual Download

1. Download the ZIP from the repo: https://github.com/justdev-chris/Mochi-AI-DISCORD/
2. Extract it anywhere you want  
3. Open terminal inside the extracted folder  
4. Run:

pip install -r requirements.txt

---

## 🔧 Setup

1. Create a `.env` file in the project root directory with the following content:

DISCORD_TOKEN=your_discord_bot_token_here
CHAT_API=your_openrouter_api_key_here

- Replace `your_discord_bot_token_here` with your Discord Bot token (from Discord Developer Portal).  
- Replace `your_openrouter_api_key_here` with your OpenRouter API key (get one free at https://openrouter.ai).

---

## 🚀 Running the Bot Locally

Run this command in your terminal (make sure you're in the project directory):

python main.py

This will start the bot. If everything is set up correctly, it will log into Discord and start responding to messages.

---

## 🛠️ Hosting Tips

### Replit

1. Upload your project files to Replit or import from GitHub.  
2. Add your `.env` secrets via the Secrets tab.  
3. Set the run command to `python main.py`.  
4. Use UptimeRobot or similar to keep your bot awake 24/7.  

### Railway

1. Connect your GitHub repo to Railway.  
2. Set environment variables (`DISCORD_TOKEN` and `CHAT_API`).  
3. Deploy the project and Railway will keep it running.  

---

## 🐾 Usage

- Invite the bot to your Discord server with proper permissions (Send Messages, Read Message History).  
- Chat with it by mentioning or using commands (command is @Mochi Catboy#7208 (yourmessage) ).  
- You are able to DM the bot but make sure you always include "@Mochi Catboy#7208 (your message)"  for it to respond.

---

## 💖 Credits

Made with love by **justdev-chris**   
Powered by OpenRouter's Cypher-Alpha free model  

---

## 📄 License

Check LICENSE.md for more info.
