import json
import pywhatkit
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

now = datetime.datetime.now()
url = 'https://www.metacareers.com/jobs'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(20)  # gives an implicit wait for 20 seconds
driver.get(url)

driver.find_element(
    By.XPATH, '//*[@id="search_result"]/div/div[1]/div[2]/div[2]/div[2]/div[1]').click()
time.sleep(5)
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "_8sel")))

driver.execute_script("window.scrollTo(0, 200)")
title = driver.find_element(By.CLASS_NAME, '_8sel').text
location = driver.find_element(By.CLASS_NAME, '_8see').text

print(title)
print(location)

msg = "META" + '\n\n' + title + '\n' + location + '\n\n' + url

with open('prev.json', 'r+') as f:
    data = json.load(f)
    # data['id'] = 134 # <--- add `id` value

    if title != data["meta"]:
        pywhatkit.sendwhatmsg("+91 9667573950", msg, now.hour, now.minute + 2)
        data["meta"] = title
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part
####### database #####
# 1. title
# 2. location
