from selenium import webdriver
import os
import random
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

browser_list = [webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options) for _ in range(5)]
# driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
while True:
     browser_num = random.randint(len(browser_list))
     browser_list[browser_num].refresh()
     print("browser number", browser_num, "refreshed")
     time.sleep(random.randint(2,10))
