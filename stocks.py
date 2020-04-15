import yfinance as yf
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def price(ticker):
   try:
      ask = yf.Ticker(ticker).info['ask']
      bid = yf.Ticker(ticker).info['bid']
      return ([ask, bid])
   except:
      return None
