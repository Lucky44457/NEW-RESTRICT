# main.py

import asyncio
import logging
from shared_client import app
from pyrogram import idle

logging.basicConfig(level=logging.INFO)

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
    asyncio.run(main())
