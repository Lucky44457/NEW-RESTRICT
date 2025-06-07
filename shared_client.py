# shared_client.py

from config import API_ID, API_HASH, BOT_TOKEN, STRING, PLUGIN_DIR
from pyrogram import Client
from telethon import TelegramClient
import sys

# ✅ Pyrogram bot with plugin support
app = Client("pyrogrambot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root=PLUGIN_DIR))

# Telethon bot
client = TelegramClient("telethonbot", API_ID, API_HASH)

# Optional userbot
userbot = Client("4gbbot", api_id=API_ID, api_hash=API_HASH, session_string=STRING)


async def start_client():
    if not client.is_connected():
        await client.start(bot_token=BOT_TOKEN)
        print("Telethon bot started...")

    if STRING:
        try:
            await userbot.start()
            print("Userbot started...")
        except Exception as e:
            print(f"Invalid session string: {e}")
            sys.exit(1)

    await app.start()
    print("Pyrogram bot with plugins started.")
    return client, app, userbot
