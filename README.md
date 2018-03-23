### How to:
1. Create a new bot user and generate a token
2. Add your tokens / keys to the .env file
```
DISCORD_TOKEN=XXX
LASTFM_KEY=XXX
YT_KEY=XXX
```
3. Install dependencies
```
python3 -m pip install -U python-dotenv
python3 -m pip install -U requests
python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]
```
4. Use the generated link to invite the bot to the server
