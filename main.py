import asyncio
import logging
from pyrogram import Client
from pyrogram import idle
from config import API_ID, API_HASH, BOT_TOKEN, PLUGIN_DIR

logging.basicConfig(level=logging.INFO)

app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root=PLUGIN_DIR)
)

async def main():
    try:
        logging.info("🔄 Starting Pyrogram bot...")
        await app.start()
        logging.info("✅ Bot started successfully!")

        logging.info("🤖 Bot is now idling...")
        await idle()
        logging.info("🛑 Idle stopped. Shutting down...")

        await app.stop()
        logging.info("✅ Bot shut down cleanly.")
    except Exception as e:
        logging.error(f"❌ Exception in main: {e}", exc_info=True)

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
