from flask import Flask, request
import telebot
from config import BOT_TOKEN

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

# /start command
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Hello! Bot is alive 🚀 and running on Koyeb!")

# /help command
@bot.message_handler(commands=['help'])
def help_message(message):
    help_text = (
        "📚 Available Commands:\n"
        "/start - Check if bot is alive\n"
        "/help - Show this message\n"
        "/batch - Handle batch task\n"
        "/login - Start login process\n"
        "/session - Create a session\n"
        "/single - Handle single task"
    )
    bot.reply_to(message, help_text)

# /batch command
@bot.message_handler(commands=['batch'])
def batch_message(message):
    bot.reply_to(message, "✅ Batch command is working!")

# /login command
@bot.message_handler(commands=['login'])
def login_message(message):
    bot.reply_to(message, "🔐 Login command is working!")

# /session command
@bot.message_handler(commands=['session'])
def session_message(message):
    bot.reply_to(message, "💬 Session command is working!")

# /single command
@bot.message_handler(commands=['single'])
def single_message(message):
    bot.reply_to(message, "🎯 Single command is working!")

# Run Flask app on port 8080
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
