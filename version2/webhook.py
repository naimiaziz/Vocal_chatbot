import os,sys
from flask import Flask,request

from flask_assistant import Assistant, ask, tell
import logging
logging.getLogger('flask_assistant').setLevel(logging.DEBUG)
CLIENT_ACCESS_TOKEN='848886a235e64039992ffd0d84829a92'
DEV_ACCES_TOKEN='101bcd629948464e889eaf9ee3a28b9a'

app = Flask(__name__)
assist = Assistant(app, route='/')


@assist.action('greeting')
def greet_and_start():
    speech = "Hey! Are you male or female?"
    return ask(speech)
    
@assist.action("give-gender")
def ask_for_color(gender):
    print("##############")
    print(assist.request)
    if assist.request['result']['resolvedQuery'] == "male":
        gender_msg = 'Sup bro!'
    else:
        gender_msg = 'Haay gurl!'

    speech = gender_msg + ' What is your favorite color?'
    return ask(speech)

@assist.action('give-color', mapping={'color': 'sys.color'})
def ask_for_season(color):
    speech = 'Ok, {} is an okay color I guess'.format(color)
    return ask(speech)

if __name__ == '__main__':
    app.run(debug=True,port=5000)


