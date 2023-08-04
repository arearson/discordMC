from discordBot import DBot
import discord
import json


def main():
    with open('secrets.JSON', 'r') as F:
        secrets = json.load(F)
    intents = discord.Intents.default()
    intents.message_content = True
    client = DBot(intents=intents)
    client.run(secrets['discord_key'])

if __name__ == '__main__':
    main()