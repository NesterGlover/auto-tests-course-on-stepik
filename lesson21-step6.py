from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("img")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    answer_input = browser.find_element_by_css_selector("input#answer")
    answer_input.send_keys(y)

    label_robot = browser.find_element_by_css_selector("#robotCheckbox")
    label_robot.click()

    label_robotsrule = browser.find_element_by_css_selector("#robotsRule")
    label_robotsrule.click()
    
    button = browser.find_element_by_css_selector("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()