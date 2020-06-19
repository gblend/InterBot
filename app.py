#imports
from flask import Flask, render_template, request, url_for
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

#create chatbot
interBot = ChatBot("InterBot", storage_adapter="chatterbot.storage.SQLStorageAdapter", database_uri='sqlite:///interbot.db',
                         logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],)
trainer = ChatterBotCorpusTrainer(interBot)
trainer.train("chatterbot.corpus.english")

#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    if userText is not None and userText != '':
        try:
            return str(interBot.get_response(userText))
        except(KeyboardInterrupt, EOFError, SystemExit):
            return 'Please enter a chat'
    


if __name__ == "__main__":
    app.run(debug=True)