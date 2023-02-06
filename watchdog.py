import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

url = os.environ['URL']
unavailble_msg = os.environ['UNAVAILABLE_MSG']


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
  # return string
  if string == unavailble_msg:
    return True
  else:
    return False
