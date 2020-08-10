# Import required libraries
import logging
from flask import Flask, request
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher

# Stepwise approach

# 1. Enable Logging
logging.basicConfig(format ='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
logger = logging.getLogger(__name__)

# My Bot Token
TOKEN = "1254283430:AAG2GPKAfygKbIYIZug3KHu3hxqeUsrpWoU"

# Creating an app object
app = Flask(__name__)

# Creating view/endpoint where requests can be recieved
@app.route('/')
def index():
	return "Hello"     # return hello at the url

# Creating view for telegram
@app.route(f'/{TOKEN}', methods=['GET', 'POST'])

def webhook():
	''' webhook view which recieves update from telegram'''
	# create update object from json-format request data
	update = telegram.Update.de_json(request.get_json(), bot)
	# processing updates
	dp.process_update(update)
	return "ok"

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

if __name__ == "__main__":
	# Set up webhook
	# Create a bot object
	bot = telegram.Bot(TOKEN)
	bot.set_webhook("https://62136476ff76.ngrok.io/" + TOKEN)


	# 3. Create a Dispatcher
	dp = Dispatcher(bot, None)

	# 4. Add Handlers
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", _help))
	dp.add_handler(MessageHandler(Filters.text, echo_text))
	dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
	dp.add_error_handler(error)

	app.run(port=8443)