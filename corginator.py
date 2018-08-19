import tweepy
import time
from random import randint
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

greetings = ['Did someone ask for a Corgi picture?', 'Here\'s a Corgi to liven up your day.', 'Corgis are awesome, aren\'t they? No wonder the Queen of England loves them.']

def send_corgi(username, status_id):
	greeting_id = randint(0, len(greetings) - 1)
	api.update_with_media('corgi.png', status = '@{} {}'.format(username, greetings[greeting_id]), in_reply_to_status_id = status_id)


for follower in tweepy.Cursor(api.followers).items():
	follower.follow()

class BotStreamer(tweepy.MyStreamListener):
	def on_status(self, status):
		username = status.user.screen_name
		status_id = status.status_id

myStreamListener = BotStreamer()
myStream = tweepy.Stream(auth, myStreamListener)
myStream.filter(track=['@corginatorbot'])