from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
browser.get(link)

treasure = browser.find_element_by_id("treasure")
valuex = treasure.get_attribute("valuex")



answer = browser.find_element_by_id("answer")
answer.send_keys(calc(valuex))

robot_check = browser.find_element_by_id("robotCheckbox")
robot_check.click()

rule_check = browser.find_element_by_id("robotsRule")
rule_check.click()

submit = browser.find_element_by_tag_name("button")
submit.click()

time.sleep(100)
browser.quit()
