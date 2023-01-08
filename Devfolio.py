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

url = 'https://devfolio.co/hackathons'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(10)  # gives an implicit wait for 20 seconds
driver.get(url)

driver.execute_script("window.scrollTo(0, 600)")
time.sleep(5)
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="__next"]/div[3]/section[1]/div[2]')))

Hackathons = driver.find_element(
    By.XPATH, '//*[@id="__next"]/div[3]/section[1]/div[2]')

link = Hackathons.find_element(By.TAG_NAME, 'a').get_attribute('href')
heading = Hackathons.find_element(By.TAG_NAME, 'h3').text
# desc = Hackathons.find_element(
#     By.CSS_SELECTOR, 'div.kJYDuD')
# info = desc.find_elements(By.TAG_NAME, 'p')
# theme = Hackathons.find_element(By.CLASS_NAME, 'bybCkV').text

# information = ""
# for i in info:
#     information += i.text
#     information += " | "

print(heading)
print(link)

msg = heading + '\n' + link

with open('prev.json', 'r+') as f:
    data = json.load(f)
    # data['id'] = 134 # <--- add `id` value

    if heading != data["amazon"]:
        pywhatkit.sendwhatmsg("+91 9667573950", msg, now.hour, now.minute + 2)
        data["amazon"] = heading
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part
# print(theme)
# print(information)

###### for database ######
# 1. heading
# 2. link
