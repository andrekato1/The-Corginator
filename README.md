# The Corginator Bot
This is a Twitter bot created using the Tweepy library for Python. This project has been created strictly for entertainment and study purposes.

## Requirements

* Python 3.6 or older
* Tweepy
* PIL

## Default behavior

Upon being mentioned in a reply to a tweet, the bot will reply a picture of a Corgi with the text from the replied tweet.
This also works when the bot is mentioned in a standalone tweet (i.e. not in reply to any tweet) and should also work with retweets.
The bot does not answer to any keywords, instead, it tracks for the word "@CorginatorBot". This causes some weird/unintended behavior which I could not figure how to circumvent. More on that in the next session.

## Known issues

The bot shouldn't be replying to replies to its original tweet. However this comes as a natural consequence of tracking its own username in the stream. An alternative could be tracking a hashtag like "#CorginatorBot" instead of "@CorginatorBot".
