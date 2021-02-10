from textblob import TextBlob

from pyrogram import Client
from os import environ

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
bot_token = environ["BOT_TOKEN"]

app = Client("my_bot",
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token)

# language = 'hi'

@app.on_message()
def message(client, message):
    lang = TextBlob(message.text)
    if (lang.detect_language) == "hi":
        # app.delete_messages(chat_id, message_id)
#         print(message)
        app.send_messaage(message.from_user.id, message)
        print(message.text,'======', message.from_user.first_name)
app.run()

