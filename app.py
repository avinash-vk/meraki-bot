from flask import Flask,jsonify,request,Response,render_template,send_file
from wit import Wit
import secrets


app = Flask(__name__)

access_token = secrets.WIT_ACCESS_TOKEN

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/test')
def botTest():
    return render_template('test.html')

@app.route('/api/bot/<message>')
def chatbot(message):
    client = Wit(access_token)
    bot_response = client.message(message)
    
    entity = bot_response['entities']
    intent = ''
    sentiment = ''
        
    if bot_response['intents']:
        intent = bot_response['intents'][0]['name']

    if bot_response['traits'] and bot_response['traits']['wit$sentiment']:
        sentiment = bot_response['traits']['wit$sentiment'][0]['value']

    chat_response = 'Hmm..'

    if intent == 'meraki_info':
        chat_response = 'Meraki is bridging gaps between jobs and people for the needy.'
    
    elif sentiment == 'negative':
        chat_response = 'Why you sad?'

    response = dict()
    response['bot_response'] = bot_response
    response['chat_response'] = chat_response
    
    return response

#comment below call for local setup
if __name__ == '__app__':
     app.run() 
