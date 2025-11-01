from telegram.ext import Updater, CommandHandler

# Replace YOUR_BOT_TOKEN with your actual bot token from BotFather
BOT_TOKEN = "8326888145:AAHopqVa982fJfIl5KPITbfN1L6w5po8AMY"

def start(update, context):
    update.message.reply_text("Hello! I'm a simple Telegram bot.")

def help(update, context):
    update.message.reply_text("Hey Me kr rha hu ghisayi.")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))


    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()