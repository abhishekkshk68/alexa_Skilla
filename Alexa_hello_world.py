from flask import Flask
from flask_ask import Ask, statement, question, session


app = Flask(__name__)
ask = Ask(app, "/test")


@app.route('/')
def homepage():
    return "hi there, how ya doin?"

@ask.launch
def start_skill():
    welcome_message = 'Are you new to DCU?'
    return question(welcome_message)

@ask.intent("YesIntent")
def share_headlines():
    #headlines = get_headlines()
    headline_msg = 'Hello, Welcome to DCU'
    return statement(headline_msg)

@ask.intent("NoIntent")
def no_intent():
    bye_text = 'I am not sure why you asked me to run then, but okay... bye'
    return statement(bye_text)

@ask.intent("Dont")
def confused():
    confused_test="Dont be confused, you are with me"
    return statement(confused_test)

if __name__ == '__main__':
    app.run(debug=True)