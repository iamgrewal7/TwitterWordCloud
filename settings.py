from dotenv import load_dotenv
import logging
import os
from tweepy import OAuthHandler

load_dotenv()

auth = OAuthHandler(
  consumer_key=os.getenv("CONSUMER_KEY"),
  consumer_secret=os.getenv("CONSUMER_SECRET")
)
auth.set_access_token(
  key=os.getenv("ACCESS_TOKEN"),
  secret=os.getenv("ACCESS_TOKEN_SECRET")
)


logging.basicConfig(filename='error.log', filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')