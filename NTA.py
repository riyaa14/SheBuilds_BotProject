import json
import pywhatkit
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

now = datetime.datetime.now()
url = 'https://nta.ac.in/'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(10)  # gives an implicit wait for 20 seconds
driver.get(url)

driver.execute_script("window.scrollTo(0, 400)")
time.sleep(5)
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="maincont"]/div/div/div[3]/div[1]/div[2]/div[2]/marquee')))

updateSection = driver.find_element(
    By.XPATH, '//*[@id="maincont"]/div/div/div[3]/div[1]/div[2]/div[2]/marquee')

title = updateSection.find_element(By.TAG_NAME, 'content').text
docs = updateSection.find_element(By.TAG_NAME, 'a').get_attribute('href')

print(title)
print(docs)

msg = "NTA" + '\n\n' + title + '\n' + docs + '\n\n' + url

with open('prev.json', 'r+') as f:
    data = json.load(f)
    # data['id'] = 134 # <--- add `id` value

    if title != data["NTA"]:
        pywhatkit.sendwhatmsg("+91 9667573950", msg, now.hour, now.minute + 2)
        data["NTA"] = title
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

####### for database #######
# 1. title
# 2. docs
