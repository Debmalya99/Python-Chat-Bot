from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from flask import Flask,jsonify
import json
import pickle

# Create a new chat bot named Charlie
chatbot = ChatBot('Customer Care')

trainer = ListTrainer(chatbot)
corpus_list = []

with open("corpus.bin","rb") as bin_file:
    corpus = pickle.load(bin_file)
    corpus_list = corpus

trainer.train(corpus_list)


app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to the landing page of the ChatBot</h1>"

@app.route("/api/customercare/<req>",methods = ['GET'])
def process_request(req):
    # req is the request
    request_dict = json.loads(req)
    response = chatbot.get_response(request_dict['request'])
    return jsonify({"response":str(response)})


if __name__ == "__main__":
    app.run(host='0.0.0.0')