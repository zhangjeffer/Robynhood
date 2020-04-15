from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from stocks import *

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    req = request.values
    msg = ""

    from_number = req.get('From') 
    body = req.get('Body') #message 
    stock_info = price(body)

    if not stock_info:
        msg = "Invalid request"
    else:
        msg = "${}: Ask: ${}, Bid: ${}".format(body, stock_info[0], stock_info[1])
    resp.message(msg)
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
