from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
browser.get("http://suninjuly.github.io/selects1.html")

result = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(result))

browser.find_element_by_css_selector('[type="submit"]').click()

time.sleep(100)
browser.quit()
