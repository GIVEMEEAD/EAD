from selenium import webdriver
import os
import random
import time
from fastapi import FastAPI,BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

def run_refresher():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    # browser_list = [webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options) for _ in range(2)]
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
    while True:
        driver.get("https://www.bilibili.com/video/BV1JV411r7m9?from=search&seid=85324665481620243")
        driver.refresh()
        print("browser refreshed")
        time.sleep(random.randint(100,120))

app = FastAPI()

@app.get("/")
def run(back:BackgroundTasks):
    back.add_task(run_refresher)
    return JSONResponse('True')
