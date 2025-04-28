#Напишите декоратор log_calls, который записывает в файл время вызова, имя и аргументы вызванной функции. 
# Один вызов функции - одна строка в файле. 
# Декоратор должен принимать имя файла для записи в качестве параметра. - С этим не очень понятно...
from functools import  wraps
import inspect
import datetime
def log_calls (func):
    @wraps(func)
    def wrapper (*args, **kwargs):
        result = func(*args, **kwargs)
        fh = open('log_calls.txt', 'w')
        fh.write(f"Время вызова: {datetime.datetime.now()}" + f" Вызвана функция: {func.__name__}"
                 + f" Получены аргументы: {inspect.signature(func)}" + "\n")
        fh.close()
        print(f"Время вызова: {datetime.datetime.now()}")
        print(f"Вызвана функция: {func.__name__}")
        print(f"Получены аргументы: {inspect.signature(func)}")
        
        return result
    return wrapper
@log_calls
def add(a, b):
    print(a+b)

add(5, 10)
with open('log_calls.txt', 'r') as fh:
  print(fh.readlines())