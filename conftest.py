from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
web = webdriver.Chrome()
import test
import time



@pytest.fixture()
def browser():
    options = Options() #Запускать в безголовом режиме (невидимка)
    options.add_argument('--headless') #Запускать в безголовом режиме (невидимка)
    browser = webdriver.Chrome(options=options) #Запускать в безголовом режиме (невидимка)
    browser = webdriver.Chrome()
    browser.maximize_window() #открытие в полном окне
    browser.implicitly_wait(10) #Включает неявное ожидание в течение 10 сек. Не сразу упадет, а подождет 10 сек.
    yield browser #возвращает
    browser.close() #постусловие, закрытие браузера