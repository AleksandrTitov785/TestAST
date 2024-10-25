from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
browser = webdriver.Chrome()



def test_click():
    browser.get('https://www.qa-practice.com/elements/button/simple') #Открыть браузер с сайтом
    # TODO Поиск по ID
    # click_button = browser.find_element(By.ID, 'submit-id-submit')
    # click_button.click()
    # TODO Поиск по Классу
    # click_button2 = browser.find_element(By.CLASS_NAME, 'btn-primary')
    # click_button2.click()
    # TODO Поиск по Тексту
    # link = browser.find_element(By.LINK_TEXT, 'Contact').click()
    # sleep(2)
    # TODO Поиск по ЦСС
    # click_button3 = browser.find_element(By.CSS_SELECTOR, 'input[class="btn btn-primary"]')
    # click_button3.click()
    # TODO Поиск по Хпаз
    click_button4 = browser.find_element(By.XPATH, '//input[@class="btn btn-primary"]')
    click_button4.click()

