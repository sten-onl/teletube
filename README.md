# Teletube

>A Python Telegram bot for your group or yourself to save YouTube videos in a common playlist

This is a Telegram bot using the [Telegram Bot API](https://core.telegram.org/bots/api) and the Python implementation [pyTelegramBotAPI](https://pytba.readthedocs.io/en/latest/index.html).

At the moment, the Bot can take user input in the form of YouTube links and save them in a .csv. By using the command /group a link at random can be send back to the user requesting it.

## Commands

`/start` - Starts the Bot and displays a welcome message with commands

`/help` - Displays the welcome message again

`/group` - Sends a random Video saved in the group.csv

`/user` - Sends a random Video saved in the user.csv

## Installation & Hosting

1. Create a new Telegram Bot using the @Botfather chat
2. Change the privacy settings for the bot so it can react to YouTube links without the /. Use /mybots and select your Bot > Bot Settings > Group Privacy > Turn off
3. Copy the generated Bot API Key and save it in the config.py
4. Save the files on the device or server where you want to run the Bot (this can be easily run on platforms like PythonAnywhere or Heroku)
5. Install the dependency using `pip install pyTelegramBotAPI`
6. Run the Bot with `python teletube.py`


## Future features
- [ ] Ability to save the videos directly in a YouTube playlist using the YouTube API
- [ ] Ability for users to create their own playlists in the chat client and adding more random options
- [ ] Display stats regarding user contributions

## How to contribute

If you would like to contribute to the project just do a pull request and I will review it


