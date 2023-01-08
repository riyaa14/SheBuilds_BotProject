import json
import pywhatkit
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

now = datetime.datetime.now()

url = 'https://jacdelhi.admissions.nic.in/'

driver = webdriver.Chrome()
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(10)  # gives an implicit wait for 20 seconds
driver.get(url)

updatesSection = driver.find_element(By.CLASS_NAME, 'gen-list')
title = updatesSection.find_element(By.TAG_NAME, 'a').text
link = updatesSection.find_element(By.TAG_NAME, 'a').get_attribute('href')

print(title)
print(link)

msg = "JAC DELHI" + '\n\n' + title + '\n' + link + '\n\n' + url

with open('prev.json', 'r+') as f:
    data = json.load(f)
    # data['id'] = 134 # <--- add `id` value

    if title != data["jac"]:
        pywhatkit.sendwhatmsg("+91 9667573950", msg, now.hour, now.minute + 2)
        data["jac"] = title
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

##### for database ####
# 1. title
# 2. link
