from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="/Users/zubair/Downloads/chromedriver")
driver.get("http://www.target.com")
assert "Target : Expect More. Pay Less." in driver.title

#--- By CSS Selector
#searchbox = driver.find_element_by_css_selector("#search")

#--- By ID
#searchbox = driver.find_element_by_id("search")

#--- By name
#searchbox = driver.find_element_by_name("searchTerm")

#-- By xpath
#searchbox = driver.find_element_by_xpath("//input[@id='search']")

driver.find_element_by_xpath("//a[@href='#accountMenu']").click()
time.sleep(5)
driver.find_element_by_xpath("//li[@id='accountNav-signIn']").click()
driver.find_element_by_xpath("//input[@autocomplete='username']").send_keys('zubairali78')
driver.find_element_by_xpath("//input[@type='password']").send_keys('qwertyuiop')
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)
driver.quit()