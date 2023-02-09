import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = os.environ['URL']
unavailble_msg = os.environ['UNAVAILABLE_MSG']


def get_changes():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')

  # instantiate driver
  driver = webdriver.Chrome(options=chrome_options)

  # get the entire website content
  driver.get(url)
  delay = 10  # seconds

  global element
  try:
    element = WebDriverWait(driver, delay).until(
      EC.presence_of_element_located(
        (By.CLASS_NAME, 'office-form-info-title'))).text
    print("Page is ready!")
  except:
    print("Loading took too much time!")
    return "Element not found. Visit ASAP"
  else:
    if element == unavailble_msg:
      return "Unavailable"
    else:
      return "Something's changed. Visit ASAP"
