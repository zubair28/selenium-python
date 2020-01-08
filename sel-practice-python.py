from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path="/Users/zubair/Downloads/chromedriver")
driver.get("http://automationpractice.com/index.php")
assert "My Store" in driver.title

#==================CREATE ACCOUNT=================

driver.find_element_by_xpath("//a[@class='login']").click()
driver.find_element_by_xpath("//input[@name='email_create']").send_keys('shermali78@gmail.com')
driver.find_element_by_xpath("//i[@class='icon-user left']").click()
time.sleep(3)

driver.find_element_by_xpath("//label[@for='id_gender1']").click()
driver.find_element_by_id("customer_firstname").send_keys('Herm')
driver.find_element_by_id("customer_lastname").send_keys('Mack')
#driver.find_element_by_id("email").send_keys('shermali78@gmail.com')
driver.find_element_by_id('passwd').send_keys('12345')
#driver.find_element_by_id("days").click()
select = Select(driver.find_element_by_id("days"))
select.select_by_value('15')
select = Select(driver.find_element_by_id("months"))
select.select_by_index('5')
select = Select(driver.find_element_by_id("years"))
select.select_by_value('1994')
time.sleep(3)

#==============ADDRESS=================

driver.find_element_by_id("company").send_keys('Crescent')
driver.find_element_by_id("address1").send_keys('123 Crescent rd')
driver.find_element_by_id("city").send_keys('Colorado Springs')
select = Select(driver.find_element_by_id("id_state"))
select.select_by_visible_text('Colorado')
driver.find_element_by_id("postcode").send_keys('80831')
driver.find_element_by_id("phone_mobile").send_keys('123 456 6780')
time.sleep(5)

#============Register================

#driver.find_element_by_xpath("//button[@id='submitAccount']").click()

driver.quit()





