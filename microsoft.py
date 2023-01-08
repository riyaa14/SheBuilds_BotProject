# /html/body/div[2]/div[2]/div/div[2]/div[1]/section[1]/div/div/div[3]/div[3]/div[1]/span/button
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
# from webdriver_manager.chrome import ChromeDriverManager

now = datetime.datetime.now()
url = 'https://careers.microsoft.com/students/us/en/search-results'

# driver = webdriver.Chrome()


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(10)  # gives an implicit wait for 20 seconds
driver.get(url)

driver.find_element(
    By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/section[1]/div/div/div[3]/div[3]/div[1]/span/button').click()
driver.find_element(
    By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[1]/section[1]/div/div/div[3]/div[3]/div[2]/div/div[3]/ul/li[8]/label/span[1]').click()

time.sleep(5)
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "information")))

driver.execute_script("window.scrollTo(0, 200)")
update = driver.find_element(By.CLASS_NAME, 'information')
heading = update.find_element(By.TAG_NAME, 'a').text
additionalInfo = update.find_elements(By.TAG_NAME, 'span')

print(heading)

desc = ""
for info in additionalInfo:
    desc += info.text
    desc += '\n'

print(desc)

msg = "MICROSOFT" + '\n\n' + heading + '\n' + desc + '\n\n' + url

with open('prev.json', 'r+') as f:
    data = json.load(f)
    # data['id'] = 134 # <--- add `id` value

    if heading != data["microsoft"]:
        pywhatkit.sendwhatmsg("+91 9667573950", msg, now.hour, now.minute + 2)
        data["microsoft"] = heading
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

####### for database ########
# 1. heading
# 2. desc
