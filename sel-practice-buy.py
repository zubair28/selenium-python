from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="/Users/zubair/Downloads/chromedriver")
driver.get("http://automationpractice.com/index.php")
assert "My Store" in driver.title
driver.find_element_by_id("search_query_top").send_keys('dress')
driver.find_element_by_name("submit_search").click()
driver.find_element_by_xpath("//img[@class='replace-2x img-responsive']").click()
driver.find_element_by_xpath("//span[text()='Add to cart']").click()
time.sleep(5)
driver.find_element_by_xpath("//a[@title='Proceed to checkout']").click()
time.sleep(5)
driver.find_element_by_xpath("//a[@class='button btn btn-default standard-checkout button-medium']").click()
driver.quit()









