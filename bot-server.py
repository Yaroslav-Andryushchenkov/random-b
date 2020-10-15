from telegram.ext import Updater
import random
import simpleneighbors
import tensorflow.compat.v2 as tf
import tensorflow_hub as hub
from tensorflow_text import SentencepieceTokenizer

def predict(question):
  query_embedding = model.signatures['question_encoder'](tf.constant([question]))['outputs'][0]
  return random.choice(index.nearest(query_embedding, n=3))

model = hub.load('./')
index = simpleneighbors.SimpleNeighbors(512)
index = index.load('./data.pickle')




updater = Updater(token='1391364191:AAHfTcFijZGZAQGH6rw6Uz8b9szQf0UYeLM', use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Осторожно! Этот бот обучен на архиве _random_b чата. (предложения о работе присылать сюда: 7098013@gmail.com)")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)



def handle_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=predict(update.message.text))

from telegram.ext import MessageHandler, Filters
message_handler = MessageHandler(Filters.text & (~Filters.command), handle_message)
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle()
updater.stop()

