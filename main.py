from flask import Flask, request
import telebot
from config import BOT_TOKEN
import os
import importlib

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

# Initialize Flask app
app = Flask(__name__)

# Your Koyeb public URL + webhook endpoint
WEBHOOK_URL = 'https://wooden-andi-lakshaykhajuria215-ac33ecfb.koyeb.app/my-bot'

# Set webhook
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL)

# Webhook endpoint
@app.route('/my-bot', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return '', 200
    else:
        return '', 403

# Basic command for checking bot status
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Hello! Bot is alive 🚀 and running on Koyeb!")

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(message, "Send /start to check if I am running!")

# === Auto-import all plugins ===
plugin_folder = "plugins"
for filename in os.listdir(plugin_folder):
    if filename.endswith(".py") and not filename.startswith("__"):
        importlib.import_module(f"{plugin_folder}.{filename[:-3]}")

# === Start Flask app ===
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
