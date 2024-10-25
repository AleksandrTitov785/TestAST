print()
import random
my_list = ['text', 'one', 'two']
print(random.choice(my_list))


import datetime
import time
import pytest

@pytest.fixture()
def before_after():
    print('Before test') #предусловие
    yield None #место для запуска теска
    print('\nAfter test') #\n - перенос строки, чтобы не сливалось ничего

def test_demo1():
    assert 1 == 1

def test_demo2(before_after):
    assert 2 == 2
import math


