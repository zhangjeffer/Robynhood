from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from stocks import *
from app import *


app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    req = request.values
    from_number = req.get('From') 
    body = req.get('Body') #message 
    msg = msg_handler(from_number, body)
    resp.message(msg)
    return str(resp)

 
if __name__ == "__main__":
    app.run(debug=True)
