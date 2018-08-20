# The Corginator Bot
This is a Twitter bot created using the Tweepy library for Python. This project has been created strictly for entertainment and study purposes.

## Requirements

* Python 3.6 or older
* Tweepy

**NOTE:** As of now, using Tweepy with Python 3.7 might cause you trouble. Apparently, `async` cannot be passed in as a function argument anymore in 3.7, the interpreter will throw you a SyntaxError. Using older versions of Python (i.e. 3.6 and older) fixes this issue.

## Default behavior

Upon receiving a mention, the bot will automatically pick a random picture from the `corgis` folder and a random greeting and reply to the user who mentioned the bot.
The bot does not answer to any keywords, rather, it replies to anyone any tweets which contains the word "@CorginatorBot". There is no need to explicitly ask for a photo.

## How to properly name the Corgi pictures

The way the bot chooses the picture is by choosing a random number between `1` and `n`, where `n` is the number of pictures in the `corgis` folder. The counting is made by using the `os.walk` function and iterating over all files and subdirectories.
Suppose we have 10 pictures, a random number between `1` and `10` will be chosen. Say `7` is the chosen number. Then, the file `7.jpeg` is going to be sent to the user.
Important things to note: each picture must be numbered, starting from 1 and without skipping any number. The file extension must be `.jpeg`. Not `.jpg`, not `.png`. The `corgis` folder must contain **only** the pictures, nothing else.

## TODO

There are some clear improvements that can be made to the code, especially with the authentication part.
Remove the extension and naming limitation when choosing random pictures
More interactivity and features.
