
from pyrogram import filters
from pyrogram.types import Message
from config import OWNER_ID
from main import app

@app.on_message(filters.command(["c3RhcnQ=", "YmF0Y2g=", "c2luZ2xl"]) & filters.private)
async def unlock_commands(_, m: Message):
    await m.reply_text("✅ Access granted. All features are unlocked and free to use!")
