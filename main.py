import os, discord
from watchdog import *
from discord.ext import tasks
from datetime import time
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

token = os.environ['TOKEN']

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')
  watchdog.start()


# UTC time 18:00PM = GTM+6 time 12:00AM
@tasks.loop(time=time(hour=18, minute=0, second=0))
async def watchdog():
  channel = client.get_channel(1072061023613370398)
  update = get_changes()
  await channel.send(update)


keep_alive()
client.run(token)
