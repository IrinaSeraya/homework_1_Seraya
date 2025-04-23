# Напишите декоратор cache, который кэширует результат вызова функции (сохраняет в словаре). 
# Когда функция вызывается снова с теми же аргументами, декоратор должен возвращать результат из кэша, 
# вместо того, чтобы вызывать декорированную функцию.
def cache_decorator(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
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