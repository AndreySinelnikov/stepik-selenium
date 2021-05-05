from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
browser.get("http://suninjuly.github.io/execute_script.html")

x = browser.find_element_by_id("input_value").text

input_field = browser.find_element_by_id("answer")
input_field.send_keys(calc(x))

robot_check = browser.find_element_by_css_selector("[for='robotCheckbox']")
robot_check.click()

radio_check = browser.find_element_by_css_selector("[for='robotsRule']")
browser.execute_script("return arguments[0].scrollIntoView(true);", radio_check)
radio_check.click()

submit = browser.find_element_by_css_selector("[type='submit']")
submit.click()

time.sleep(40)
browser.quit()

