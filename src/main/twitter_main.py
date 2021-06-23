import tweepy
import pandas as pd
import json


class MyStreamListener(tweepy.StreamListener):

    def on_data(self, raw_data):
        self.process_data(raw_data)
        return True

    def process_data(self, raw_data):
        print(raw_data)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False
def read_credentials():
    with open('access.env') as f:
        data = f.read()
    dict = json.loads(data)
    return dict

if __name__ == "__main__":
    key_dict = read_credentials()
    auth = tweepy.OAuthHandler(key_dict['api_key'], key_dict['api_secret_key'])
    auth.set_access_token(key_dict['access_token'], key_dict['access_token_secret'])

    listener = MyStreamListener()
    stream = tweepy.Stream(auth=auth, listener=listener)
    stream.filter(track=['python'], is_async=False)
    print("Success")
