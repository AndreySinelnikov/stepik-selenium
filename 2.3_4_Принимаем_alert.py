from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
browser.get("http://suninjuly.github.io/alert_accept.html")

browser.find_element_by_css_selector("[type='submit']").click()

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element_by_id("input_value").text
browser.find_element_by_id("answer").send_keys(calc(x))
browser.find_element_by_css_selector("[type='submit']").click()

time.sleep(30)
browser.quit()

