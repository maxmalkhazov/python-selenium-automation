from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
# by ID
driver.find_element(By.ID, 'twotabsearchtextbox')
# by XPATH
driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo']")
# using only tag
driver.find_element(By.XPATH, "//a")  # == driver.find_element(By.TAG_NAME, "a")
# using only attribute
driver.find_element(By.XPATH, "//*[@href='/ref=nav_logo']")
# using multiple attributes
driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo' and @aria-label='Amazon']")
# using partial attr
driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]")
# using multiple nodes, 1 by 1, /
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']/div/a[contains(@href, 'bestsellers')]")
# using multiple nodes, skipping nodes with //
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']//a[contains(@href, 'bestsellers')]")
# by XPATH using text
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
# Text can be combined with attributes or other nodes
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")
# by partial text, using contains:
driver.find_element(By.XPATH, "//a[contains(text(),'Best Sell') and @class='nav-a  ']")