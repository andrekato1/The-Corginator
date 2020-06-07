import tweepy
import os
from dotenv import load_dotenv
from random import choice
from imutil import Drawer

load_dotenv()

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

class TweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api

    def on_status(self, tweet):
        drawer = Drawer()
        
        reply_id = tweet.in_reply_to_status_id if tweet.in_reply_to_status_id != None else tweet.id
        status = self.api.get_status(reply_id, tweet_mode='extended')
        self.received_tweet(tweet.user.screen_name, status.full_text, tweet.in_reply_to_screen_name, tweet.created_at)

        # Only do something if the status has text in it apart from the mention itself
        if len(status.full_text) > 1:
            # Bot shouldn't reply to itself
            if status.user.screen_name != "CorginatorBot":
                text = self.remove_mentions(status.full_text)
                if "media" in status.entities:
                    text = text.rsplit(' ', 1)[0]
                drawer.draw_text(text)
                self.api.update_with_media("out.jpeg", in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)

    def received_tweet(self, author, text, in_reply_to, time):
        print("*** INCOMING TWEET ***")
        print("From: @{}\nIn reply to: @{}\nTime: {}".format(author, in_reply_to, time))
        print("Content:\n{}".format(text))
        print("**********************\n")

    def remove_mentions(self, text):
        splitted = text.split(" ")
        while splitted[0][0] == "@":
            splitted.pop(0)
        return ' '.join(splitted)

    def on_error(self, status):
        print("Deu ruim aqui amigão, me salva")
        print(status)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

listener = TweetListener(api)
stream = tweepy.Stream(api.auth, listener)
stream.filter(track=["@CorginatorBot"])