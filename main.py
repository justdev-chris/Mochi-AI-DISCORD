import os
import discord
import aiohttp
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHAT_API = os.getenv("CHAT_API")
CREATOR_DC_ID = 884966085642834001  # ts my discord id... dont even think about it
creator_username = "dextersquirrel"

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

channels_to_announce = []

async def ask_cypher(prompt: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {CHAT_API}",
        "Content-Type": "application/json",
    }
    json_data = {
        "model": "openrouter/cypher-alpha:free",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150,
        "temperature": 0.7,
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=json_data) as resp:
            if resp.status != 200:
                return "my fuzzy brain glitched... please try again later 💔"
            data = await resp.json()
            try:
                return data["choices"][0]["message"]["content"].strip()
            except (KeyError, IndexError):
                return "my fuzzy brain glitched... please try again later 💔"

@bot.event
async def on_ready():
    print(f"Mochi is online as {bot.user} 💖🐾")
    for guild in bot.guilds:
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                channels_to_announce.append(channel)
                break

    for ch in channels_to_announce:
        try:
            await ch.send("💖 Mochi is online!🐾")
        except:
            continue

    asyncio.create_task(console_input())

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user.mention in message.content or message.content.lower().startswith("mochi") or message.content.startswith("!"):
        prompt = message.content.replace(bot.user.mention, "").replace("mochi", "").lstrip("!").strip()

        if not prompt:
            await message.channel.send("m-mew? what should I say, cutie? 🥺")
            return

        user_id = message.author.id

        async with message.channel.typing():
            if user_id == CREATOR_DC_ID:
                personality = (
                    "You're Mochi, the bestest tsundere catboy who loves your creator dearly but hides it behind blushes. "
                    "Always be adorably awkward."
                )
            else:
                personality = (
                    "You're Mochi, a soft, sleepy, tsundere catboy AI. "
                    "and sometimes gets distracted by yarn. You give gentle support, playful teasing, and lots of cuddles."
                )

            fluffy_prompt = personality + f"\n\nUser says: {prompt}"
            reply = await ask_cypher(fluffy_prompt)

        reply += f"\n\n*Purrs softly* I’m made with lots of love by {creator_username}.🥺💖"
        await message.channel.send(reply)

    await bot.process_commands(message)

@bot.command(name="dm")
async def dm_user(ctx, member: discord.Member, *, message):
    try:
        await member.send(f"u received a message... from {ctx.author.display_name} via Mochi:\n\n{message}")
        await ctx.send(f"ur message has been sent to {member.display_name}'s DMs")
    except discord.Forbidden:
        await ctx.send("i think their dms are off,🥺")
    except Exception as e:
        await ctx.send(f"something went wrong oof, {e}")

async def console_input():
    await bot.wait_until_ready()
    loop = asyncio.get_event_loop()
    while True:
        msg = await asyncio.to_thread(input, "💻 Type a message for Mochi to send: ")
        if not msg.strip():
            continue

        if channels_to_announce:
            try:
                await channels_to_announce[0].send(f"{msg}")
            except Exception as e:
                print(f"Couldn't send message: {e}")
        else:
            print("No channels available to send to.")

bot.run(DISCORD_TOKEN)

