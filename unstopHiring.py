from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://unstop.com/hiring-challenges?filters=,all,open,all&types=teamsize,payment,oppstatus,eligible'

driver = webdriver.Chrome()
driver.maximize_window()  # For maximizing window
driver.implicitly_wait(10)  # gives an implicit wait for 20 seconds
driver.get(url)

Challenge = driver.find_element(By.CLASS_NAME, 'cptn')
heading = Challenge.find_element(By.TAG_NAME, 'h2').text
company = Challenge.find_element(By.TAG_NAME, 'h3').text
link = driver.find_element(By.CLASS_NAME, 'listing').get_attribute('href')

print(heading)
print(company)
print(link)

##### for database ######
# 1. heading
# 2. company
# 3. link
