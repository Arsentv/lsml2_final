import telegram
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler

telegram_bot_token = '5956945497:AAEkxlAuY9EyE0phy1PrQz4lnDFae77ZJg0'

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

# set up the introductory statement for the bot when the /start command is invoked
def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Hello there. Provide any English sentence")

def get_result(update, context):
    result = output(update.message.text)
    update.message.reply_text(result)

# run the start function when the user invokes the /start command 
dispatcher.add_handler(CommandHandler("start", start))

dispatcher.add_handler(MessageHandler(Filters.text, get_result))
updater.start_polling()
