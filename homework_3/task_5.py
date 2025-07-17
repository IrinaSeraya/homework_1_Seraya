# Напишите декоратор cache, который кэширует результат вызова функции (сохраняет в словаре). 
# Когда функция вызывается снова с теми же аргументами, декоратор должен возвращать результат из кэша, 
# вместо того, чтобы вызывать декорированную функцию.
from functools import wraps
def cache_decorator(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key in cache:
            result = cache[cache_key]
        else:
            result = func(*args)
            cache[cache_key] = result
        return result
    return wrapper

user_input = int(input('Введите число '))

@cache_decorator
def factorial(n):
  if n != 1:
    return n * factorial(n-1) 
  else:  
    return 1

print(factorial(user_input))