from pyrogram import Client

app = Client(
    "MyBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")  # <-- this loads your batch.py
)

app.run()
