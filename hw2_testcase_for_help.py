from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/maxmal/Documents/QA/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html ')

#find the element
search = driver.find_element(By.ID, "helpsearch")
search.clear()
search.send_keys('Cancel order')

# click search
search.send_keys(Keys.RETURN)

# verify
expected_result = 'Cancel Items or Orders'
actual_result = driver.find_element(By.XPATH, "//div[@class='help-content']/h1[text()='Cancel Items or Orders']").text
print(actual_result)

assert expected_result == actual_result
print('Test case passed')
driver.quit()
