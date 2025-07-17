#Напишите декоратор @rate_limit, который разрешает только X вызовов в Y секунд (например, 5 раз в 60 сек).

from functools import wraps
import time

def rate_limit(max_calls, time_frame):
    def decorator(func):
        last_called = 0
        call_count = 0
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_called, call_count
            now = time.time()
            if now - last_called >= time_frame:
                call_count = 0
                last_called = now
            if call_count < max_calls:
                call_count += 1
                return func(*args, **kwargs)
            else:
                print("Превышено ограничение вызовов. Попробуйте позже.")
        return wrapper
    return decorator

@rate_limit(2, 5)
def add(a, b):
    return a + b

print(add(6, 10))
time.sleep(4)
print(add(8, 10))
time.sleep(2)
print(add(9, 10))