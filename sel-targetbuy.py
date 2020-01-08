from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="/Users/zubair/Downloads/chromedriver")
driver.get("http://www.target.com")
assert "Target : Expect More. Pay Less." in driver.title