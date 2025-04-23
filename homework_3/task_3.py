#Напишите декоратор log_calls, который записывает в файл время вызова, имя и аргументы вызванной функции. 
# Один вызов функции - одна строка в файле. Декоратор должен принимать имя файла для записи в качестве параметра.
from functools import  wraps
import inspect
import time
def log_calls (func):
    def wrapper (*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Время вызова: {time.gmtime(time.time())}")
        print(f"Вызвана функция: {func.__name__}")
        print(f"Получены аргументы: {inspect.signature(func)}")
        
        return result
    return wrapper
@log_calls
def add(a, b):
    print(a+b)

add(5, 10)