#The skill set is Search the Pie with an account amazon of Alexa adapt
from flask import Flask
from flask_ask import Ask, statement, question, session
import ddg3
import urllib
import wikipedia

app = Flask(__name__)
ask = Ask(app, "/duck")


def search_duck(query):
    r = ddg3.query(query)
    print(r.type)
    response = "I'm sorry I can't find anything on this subject"
    if (r.type == 'answer'):
        response = r.abstract.text
    elif (r.type == 'disambiguation'):
        response = r.related[0].text
    elif (r.type == 'nothing'):
        response = r.answer.text

    return "\n" + "Duck Duck Go says " + "\n" + response


def search_wiki(query):
    summary = wikipedia.summary(query, sentences=1)
    return "\n" + "Wikipedia says " + "\n" + summary


@app.route('/')
def homepage():
    return "hi there, how ya doin?"


@ask.launch
def start_skill():
    welcome_message = 'Hello there, how can I help you ?'
    return question(welcome_message)


# Trigger by "Tell me more about something"
# "something" is a AMAZON.SearchQuery slot
@ask.intent("FindIntent", mapping={'smt': 'Something'})
def start_query(smt):
    print(smt)
    r = search_duck(smt)  # change to search_wiki to do a wikipedia search
    return statement(r)


if __name__ == '__main__':
    app.run(debug=True)
