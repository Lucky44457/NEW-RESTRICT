import asyncio
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN, PLUGIN_DIR

client = Client(
    name="my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root=PLUGIN_DIR)
)

async def main():
    await client.delete_webhook()  # ← this line is important!
    await client.start()
    print("✅ Bot started using long polling...")
    await idle()
    await client.stop()

if __name__ == "__main__":
    asyncio.run(main())
