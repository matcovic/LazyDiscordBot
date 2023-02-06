import os
import discord
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager

intents = discord.Intents.default()
intents.message_content = True

token = os.environ['TOKEN']
url = os.environ['URL']
unavailble_msg = os.environ['UNAVAILABLE_MSG']

client = discord.Client(intents=intents)


def get_updated_changes():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  # # instantiate options
  # options = webdriver.ChromeOptions()

  # # run browser in headless mode
  # options.headless = True

  # instantiate driver
  driver = webdriver.Chrome(options=chrome_options)

  # get the entire website content
  driver.get(url)

  string = driver.find_element(By.CLASS_NAME, 'office-form-info-title').text

  if string == unavailble_msg:
    return True
  else:
    return False


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('hello'):
    update = get_updated_changes()
    await message.channel.send(update)


client.run(token)
