# Imports
import csv
import json
import os
import settings
import tweepy
import logging
import sys
from tqdm import tqdm


def write_to_json(file_name, data):
  with open(file_name, 'w') as json_file:
    json.dump(data, json_file)


def write_to_csv(file_name, data):
  with open(file_name, 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['id', 'text'])
    for _id, text in data:
      writer.writerow([_id, text])

class TwitterStreamListner(tweepy.StreamListener):
  def __init__(self, file_name):
    self.api = tweepy.API()
    self.data = []
    self.remaining = 1000
    self.file_name = file_name
    self.pbar = tqdm(total=1000)

  def on_status(self, status):
    try:
      if not self.remaining:
        write_to_csv(self.file_name, self.data)
        self.pbar.close()
        print(':) Finished')
        sys.exit()

      try:
        self.data.append([status.id, status.extended_tweet["full_text"]])
      except AttributeError:
        self.data.append([status.id, status.text])

      self.remaining -= 1
      self.pbar.update(1)
    except Exception as error:
      logging.error(str(error))

  
  def on_error(self, status_code):
    logging.error(status_code)
    return False if status_code == 420 else True


def main():
  # For D1
  twitterStreamListner = TwitterStreamListner(file_name='D1.csv')
  stream = tweepy.Stream(settings.auth, twitterStreamListner)
  stream.sample(languages=['en'])

  # For D2
  twitterStreamListner = TwitterStreamListner(file_name='D2.csv')
  stream = tweepy.Stream(settings.auth, twitterStreamListner)
  stream.filter(track=['COVID-19'], languages=['en'])


if __name__ == "__main__":
  main()