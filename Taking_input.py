from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
#import unidecode
import wikipedia

app = Flask(__name__)
ask = Ask(app, "/test")


@app.route('/')
def homepage():
    return "hi there, how ya doin?"

@ask.launch
def start_skill():
    welcome_message = 'Are you Abhishek?'
    return question(welcome_message)

@ask.intent("YesIntent")
def share_headlines():
    #headlines = get_headlines()
    headline_msg = 'The current world news headlines are'
    return statement(headline_msg)

@ask.intent("NoIntent")
def no_intent():
    bye_text = 'I am not sure why you asked me to run then, but okay... bye'
    return statement(bye_text)

@ask.intent("Dont")
def confused():
    confused_test="Dont be confused, you are with me"
    return statement(confused_test)

@ask.intent("search",mapping={'query':'Query'})
def search_wik(Query):
    summary_test=wikipedia.summary(Query,sentences=1)
    return statement(summary_test)

if __name__ == '__main__':
    app.run(debug=True)