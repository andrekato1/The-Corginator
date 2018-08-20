import os
from credentials import *
from random import choice
from random import randint
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream
from tweepy import API
from tweepy import Cursor

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret) 
api = API(auth)

for follower in Cursor(api.followers).items():
    follower.follow()
    print("Followed back: {}".format(follower.screen_name))

def send_corgi(username, status_id):
	greetings = ['Did someone ask for a Corgi picture?', 'Here\'s a Corgi to liven up your day.', 'I hope you\'re having a great day. Here, have a Corgi.', 'What do you call a Corgi with three eyes? A Corgiii.', 'Why can\'t Corgis bring in the round at the pub? Because they are a bit short.', 'What did one Corgi say to another? \"Woof\".', 'What do you call a Corgi out of cash? A Pembroke!']
	image_path = "corgis/"
	number_images = sum([len(files) for r, d, files in os.walk("C:/PathToFolder/corgis")])
	image_path += "{}.jpeg".format(randint(1, number_images))
	api.update_with_media(image_path, status = '@{} {}'.format(username, choice(greetings)), in_reply_to_status_id = status_id)

class Listener(StreamListener):
	def on_status(self, status):
		username = status.user.screen_name
		status_id = status.id
		print("Received tweet.")
		send_corgi(username, status_id)

	def on_error(self, status):
		if status == 420:
			print("Whoops. 420 detected. Returning false.")
			return False
		print(status)

class Authenticator:
	def authenticate(self):
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_secret)
		return auth

class TwitterStreamer:
	def __init__(self):
		self.twitter_authenticator = Authenticator()

	def stream_tweets(self, wordlist):
		listener = Listener()
		auth = self.twitter_authenticator.authenticate()
		stream = Stream(auth, listener)
		stream.filter(track=wordlist)

if __name__ == "__main__":
	wordlist = ["@CorginatorBot"]
	streamer = TwitterStreamer()
	streamer.stream_tweets(wordlist)
