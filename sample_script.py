from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
driver = webdriver.Chrome(executable_path='/Users/maxmal/Documents/QA/python-selenium-automation/chromedriver')
driver.maximize_window()

# Implicit wait = every 0.1 sec
# if element not there => NoSuchElement Ex
# applied to find_element
# driver.implicitly_wait(5)

# Explicit wait = every 0.5 sec
# if condition not met => TimeoutEx
driver.wait = WebDriverWait(driver, 10)

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Car')

# wait for 4 sec
# sleep(4)

# click search
SEARCH_BTN = (By.NAME, 'btnK')
driver.wait.until(EC.element_to_be_clickable(SEARCH_BTN), message=f'Element not clickable by {SEARCH_BTN}').click()
# driver.find_element(By.NAME, 'btnK').click()
# verify
assert 'car' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')
driver.quit()
