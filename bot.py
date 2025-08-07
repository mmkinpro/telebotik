import random
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

phrases = [
    "Привет, я тут!",
    "Что там у вас?",
    "Да я вообще супербот!",
    "Где кофе? ☕",
    "Слышь, че делаешь?"
]

def random_reply(update: Update, context: CallbackContext):
    if random.randint(1, 4) == 1:
        update.message.reply_text(random.choice(phrases))

def main():
    import os
    token = os.environ.get('BOT_TOKEN')
    updater = Updater(token)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, random_reply))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
