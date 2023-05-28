import os, time
import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = os.environ['URL']
unavailble_msg = os.environ['UNAVAILABLE_MSG']
img_url = os.environ['IMG_URL']


def get_changes():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')

  # instantiate driverS
  driver = webdriver.Chrome(options=chrome_options)

  # get the entire website content
  driver.implicitly_wait(10)
  driver.get(url)
  # delay = 10  # seconds

  global element
  try:
    element = driver.find_element(
      By.XPATH, "//img[contains(@role,'presentation')]").get_attribute('src')
    print("Page is ready!")
    # print(element)
  except:
    print("Loading took too much time!")
    return "Element not found. Visit ASAP"
  else:
    if element == img_url:
      print("Unavailable")
      return "Unavailable"
    else:
      print("Something's changed. Visit ASAP")
      return "Something's changed. Visit ASAP"


# https://plainenglish.io/blog/web-scraping-images-with-python-and-selenium-792e452abd70
