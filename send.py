from twilio.rest import Client
import sys 
import os

account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']

client = Client(account_sid, auth_token)
client.messages.create(
   to = sys.argv[1],
   from_ = os.environ['TWILIO_NUMBER'],
   body = "Welcome to Robinhood offline!"
)

