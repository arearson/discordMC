import discord
from discordBot.serverControl import Server
import os

mc = Server((os.path.abspath('start.bat')),os.path.abspath('server'))


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    async def on_message(self,message):
        if message.content.startswith("/startserver"):
            await message.reply("Server is starting...")
            mc.start_server()
        if message.content.startswith("/stopserver"):
            await message.reply("Server is stopping...")
            mc.stop_server()


if __name__ == '__main__':
    import json
    with open('secrets.JSON', 'r') as F:
        secrets = json.load(F)
    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)
    client.run(secrets['discord_key'])