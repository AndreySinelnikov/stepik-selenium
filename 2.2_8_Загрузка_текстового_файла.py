from selenium import webdriver
import os
import time

#228_file.txt

browser = webdriver.Chrome("C:\chromedriver\chromedriver.exe")
browser.get("http://suninjuly.github.io/file_input.html")

first_name = browser.find_element_by_name("firstname")
first_name.send_keys("Robot")

last_name = browser.find_element_by_name("lastname")
last_name.send_keys("Robotsson")

email = browser.find_element_by_name("email")
email.send_keys("robotsson@gmail.com")

# путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))

# к нему добавляется имя загружаемого файла
file_path = os.path.join(current_dir, '228_file.txt')

browser.find_element_by_name("file").send_keys(file_path)

browser.find_element_by_css_selector("[type='submit']").click()

time.sleep(30)
browser.quit()
