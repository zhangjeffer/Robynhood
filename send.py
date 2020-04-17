from twilio.rest import Client
import sys 
import os

account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']

client = Client(account_sid, auth_token)
client.messages.create(
   to = sys.argv[1],
   from_ = os.environ['TWILIO_NUMBER'],
   body = "Welcome to Robynhood. Let's get started! \n\n" + 
          "To view a stock enter a ticket symbol. Ex/ $VOO \n\n" +
          "To add a stock to your watchlist use the command Add followed by the ticker symbol: Ex/ Add $VOO\n\n" +
          "To remove a stock from your watchlist use the command Remove followed by the ticker symbol: Ex/ Remove $VOO\n\n" +
          "To display your watchlist use the command Show. Ex/ Show"
)