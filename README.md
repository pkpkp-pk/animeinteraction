# Anime Interaction Python Telegram bot
## Overview
A simple bot that can **parse** anime, **search** for anime **by file** and **return random** anime.

## Commands
-  **Hello** - Test message for checking bot's functionality
- **/randomAnime** - Output random anime from file
- **/searchAnime** - Search anime in file by your input
- **/parse** - Start parsing anime from site

## Explanations
In files `bot.py` and `search.py` you need to replace `*TOKEN*` with your telegram bot token.

Same with `user_id == 123456789 or user_id == 987654321:` you need to change this id to privilaged users id.

In folder `anime_parser` and file `anime.py` you can change delay of parsing by changing `request_time` value from 7 to your **(It's not recommended to set less than 3)**.