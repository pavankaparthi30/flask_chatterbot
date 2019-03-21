from flask import Flask, render_template, request

from chatterbot import ChatBot

from chatterbot.trainers import ListTrainer
import os



app = Flask(__name__)



mvsr_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

logic_adapters=[
	
        
       {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': "I'm currently unable to answer that. Please try being more specific."
        }
    ],



trainer = ListTrainer(mvsr_bot);
for files in os.listdir('TrainingData/'):
	data=open('TrainingData/'+files,'r').readlines()
	trainer.train(data)





@app.route("/")

def home():

    return render_template("index.html")



@app.route("/get")

def get_bot_response():

    userText = request.args.get('msg')

    return str(mvsr_bot.get_response(userText))





if __name__ == "__main__":

    app.run()