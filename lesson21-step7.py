from selenium import webdriver
import time
import math
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_css_selector("[name='firstname']")
    firstname.send_keys("LEROOOOOOOOOOOOOOOOOOOOOOOY")

    lastname = browser.find_element_by_css_selector("[name='lastname']")
    lastname.send_keys("JENKINSSSSSSSSSSSSSSSSSSSSSSSS")

    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys("@")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    
    button = browser.find_element_by_css_selector("#file")
    button.send_keys(file_path)

    browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()