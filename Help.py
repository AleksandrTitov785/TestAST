#TODO Присвоение перемнной и складывание их в выводимом результате. (По 1 данных). first\second любое название может быть
first_num=1      #int
second_num=2
some_text = "my text"   #str
print(first_num+second_num)

#TODO Хранение нескольких элементов данных! new_element - любое название может быть
new_element = [2, 5, 7, 8]  #list

#TODO Можно ввести наименование, поставить . (точку) и смотреть какие есть команды

#TODO Функции. Всегда начинается с def и лучше в отдельном файле создавать! (): скобки и двоеточие пишем ВСЕГДА, они должны быть в конце!
#Слова пишем в '' ковычках
def cal():
    print('hello')

def cal1(name):
    print('hello' + name)
    cal1(name='Alex')


#TODO Предусловие и постусловие
@pytest.fixture
def before_after():
    print('Before test') #предусловие
    yield None #место для запуска теста
    print('\nAfter test') #\n - перенос строки, чтобы не сливалось ничего

#TODO #Включает неявное ожидание в течение 10 сек. Не сразу упадет, а подождет 10 сек.
 #    browser.implicitly_wait(10) #По сути таймаут

#TODO Функция len узнает количество элементов в списке (monitors)
 #    assert len(monitors) == 2  #Функция len узнает количество элементов в списке minitors

#TODO Self - обращение к странице
 #    self.browser = browser #Self - обращение к странице

#TODO Запуск тестов в невидимке (не открывать браузер визуально)
 #    options = Options() #Запускать в безголовом режиме (невидимка)
 #    options.add_argument('--headless') #Запускать в безголовом режиме (невидимка)
 #    browser = webdriver.Chrome(options=options) #Запускать в безголовом режиме (невидимка)