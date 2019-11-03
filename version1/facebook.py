import os, sys
from flask import Flask, request
from pymessenger import Bot
import dialogflow_text_dectect as dtd



app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAADZBoGksqeEBAH3BzqlQbvXNpsK9qKlH88Np3b6rvmJLiYwpmV6assFMHFuD4qbJnmzKihBOIHm1hOHRZACiT9WeI2qFUCN6lNrbP8zfrihrhyN1fptJ68JFZBhctZCPbWIyBALXJq0fUkv0pRA6PanW4CwcDvisOpGQIwaZAGfN8PsCzGDt"

bot = Bot(PAGE_ACCESS_TOKEN)

'''
@app.route('/', methods=['GET'])
def verify():
	# Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 409
        return request.args["hub.challenge"], 200
    return "Hello world", 200
'''

@app.route('/', methods=['GET'])
def handle_verification():
    if (request.args.get('hub.verify_token', '') == "hello"):
        print("Verified")
        return request.args.get('hub.challenge', '')
    else:
        print("Wrong token")
        return "Error, wrong validation token"



@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	log(data)

	if data['object'] == 'page':
		for entry in data['entry']:
			for messaging_event in entry['messaging']:

				# IDs
				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					# Extracting text message
					if 'text' in messaging_event['message']:
					    messaging_text = dtd.apiaiCon(messaging_event['message']['text'])
						
					
					# Echo
					response = messaging_text
					bot.send_text_message(sender_id, response)

	return "ok", 200


def log(message):
	print(message)
	sys.stdout.flush()


if __name__ == "__main__":
	app.run(debug = True, port = 5000)
