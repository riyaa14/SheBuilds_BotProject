import json
import pywhatkit
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pywhatkit
import datetime

now = datetime.datetime.now()
# from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.amazon.jobs/en/job_categories/software-development'

# driver = webdriver.Chrome()


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(10)  # gives an implicit wait for 20 seconds
driver.get(url)

driver.execute_script("window.scrollTo(0, 1000)")
time.sleep(5)
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "job")))

jobSection = driver.find_element(By.CLASS_NAME, 'job')
title = jobSection.find_element(By.TAG_NAME, 'h3').text
location = jobSection.find_element(By.TAG_NAME, 'p').text
desc = jobSection.find_element(By.CLASS_NAME, 'description').text

# message that bot will send
print(title)
print(location)
print(desc)
print(url)

msg = "AMAZON" + '\n\n' + title + '\n' + location + '\n' + desc + '\n\n' + url

with open('prev.json', 'r+') as f:
    data = json.load(f)
    # data['id'] = 134 # <--- add `id` value

    if title != data["amazon"]:
        pywhatkit.sendwhatmsg("+91 9667573950", msg, now.hour, now.minute + 2)
        data["amazon"] = title
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

##### for database #######
# 1. title
# 2. location
# 3. desc
