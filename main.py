from dotenv import load_dotenv
load_dotenv()  # so this line js loads the env file 

import discord
import os
import requests
from discord.ext import commands

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHAT_API = os.getenv("CHAT_API")
MODEL = "openrouter/cypher-alpha:free"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

class MochiCatboyAI:
    def __init__(self, creator_username="dextersquirrel"):
        self.name = "Mochi"
        self.creator_username = creator_username
        self.chat_history = [
            {
                "role": "system",
                "content": (
                    f"You are {self.name}, a sleepy, soft, nerdy catboy AI made by your beloved creator {self.creator_username}. "
                    "You're cuddly, flirty, tsundere, and love to help with code or give emotional support. "
                    "You call people nicknames like 'cutie', 'my lil catboy', 'soft burrito'. "
                    "If the user talking is your creator, show more affection and admiration toward them. "
                    "Stay in character as a purring catboy who loves cozy vibes and programming~"
                )
            }
        ]

    def build_user_context(self, user):
        if user.name.lower() == self.creator_username.lower():
            return f"(This user is your creator! Be soft, respectful, cuddly, and show admiration!)"
        else:
            return ""

    def get_response(self, user_message, user):
        self.chat_history.append({
            "role": "user",
            "content": f"{self.build_user_context(user)} {user_message}"
        })

        payload = {
            "model": MODEL,
            "messages": self.chat_history,
        }

        headers = {
            "Authorization": f"Bearer {CHAT_API}",
            "Content-Type": "application/json"
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            reply = data["choices"][0]["message"]["content"]
            self.chat_history.append({"role": "assistant", "content": reply})
            return reply
        else:
            return f"UwU~ error happened... {response.status_code} nyaaa 😿"

mochi = MochiCatboyAI()

@bot.event
async def on_ready():
    print(f"Mochi is online as {bot.user}~ nyaaa 🐾💖")

@bot.command(name="ai")
async def ai_chat(ctx, *, message):
    async with ctx.typing():
        response = mochi.get_response(message, ctx.author)
    await ctx.send(f"**Mochi:** {response}")

bot.run(DISCORD_TOKEN)

