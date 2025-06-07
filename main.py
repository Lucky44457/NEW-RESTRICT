import os
import asyncio
import importlib
from flask import Flask, request, render_template
from threading import Thread
import telebot

# == Flask App Setup ==
app = Flask(__name__)
bot_token = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN")  # safe default
bot = telebot.TeleBot(bot_token)

@app.route("/")
def welcome():
    return render_template("welcome.html")  # Optional

@app.route("/my-bot", methods=["POST"])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_str = request.get_data().decode("utf-8")
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return '', 200
    return 'Invalid content type', 403

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Hello from merged bot!")

# == Async Plugin Loader ==
async def load_plugins():
    from shared_client import start_client
    await start_client()

    plugin_dir = "plugins"
    plugins = [f[:-3] for f in os.listdir(plugin_dir) if f.endswith(".py") and f != "__init__.py"]

    for plugin in plugins:
        module = importlib.import_module(f"plugins.{plugin}")
        if hasattr(module, f"run_{plugin}_plugin"):
            print(f"Running {plugin} plugin...")
            await getattr(module, f"run_{plugin}_plugin")()

# == Run Flask in a Thread ==
def run_flask():
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting Flask server on port {port}")
    app.run(host="0.0.0.0", port=port)

# == Main Entrypoint ==
if __name__ == "__main__":
    # Start webhook setup
    webhook_url = os.environ.get("WEBHOOK_URL", "https://your-koyeb-url.koyeb.app/my-bot")
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)

    # Start Flask in a thread
    Thread(target=run_flask).start()

    # Start asyncio event loop for plugin runner
    loop = asyncio.get_event_loop()
    print("Starting async plugins ...")
    try:
        loop.run_until_complete(load_plugins())
        loop.run_forever()
    except KeyboardInterrupt:
        print("Shutting down...")
    except Exception as e:
        print(f"Error: {e}")
