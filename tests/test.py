from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from operis.log import log

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
driver.close()
