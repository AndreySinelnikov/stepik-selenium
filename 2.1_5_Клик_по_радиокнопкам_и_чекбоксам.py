from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
browser.get(link)

x_elem = browser.find_element_by_id("input_value")
# достаём текст из элемента
x = x_elem.text
y = calc(x)

answer = browser.find_element_by_id("answer")
answer.send_keys(y)

robot_check = browser.find_element_by_id("robotCheckbox")
robot_check.click()

rule_check = browser.find_element_by_id("robotsRule")
rule_check.click()

submit = browser.find_element_by_tag_name("button")
submit.click()

time.sleep(10)
browser.quit()




