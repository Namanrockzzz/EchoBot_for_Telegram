# Import required libraries
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Stepwise approach

# 1. Enable Logging
logging.basicConfig(format ='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger(__name__)

# My Bot Token
TOKEN = "1254283430:AAG2GPKAfygKbIYIZug3KHu3hxqeUsrpWoU"

# Define start function for command /start
def start(bot,update):
	print(update)
	author = (update.message.from_user.first_name)
	reply = "Hi! {}".format(author)
	bot.send_message(chat_id=update.message.chat_id, text = reply)

# Define help function for command /help
def _help(bot, update):
	help_text = "Hey! this is a help text"
	bot.send_message(chat_id=update.message.chat_id, text = help_text)

# Define echo_text for any text sent by a user
def echo_text(bot, update):
	reply = update.message.text
	bot.send_message(chat_id=update.message.chat_id, text = reply)

# Define echo_sticker for any sticker sent by a user
def echo_sticker(bot, update):
	bot.send_sticker(chat_id=update.message.chat_id, sticker = update.message.sticker.file_id)

def error(bot, update):
	logger.error("Update '%s' caused error '%s'", update, update.error)


# Define main function
def main():
	# 2. Create Updater
	updater = Updater(TOKEN)

	# 3. Create a Dispatcher
	dp = updater.dispatcher

	# 4. Add Handlers
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", _help))
	dp.add_handler(MessageHandler(Filters.text, echo_text))
	dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
	dp.add_error_handler(error)

	# 5. Start Poling and wait for any signal to end the program
	updater.start_polling()
	logger.info("Started Polling...")
	updater.idle()   # Waits until a user presses ctrl+c




if __name__ == "__main__":
	main()