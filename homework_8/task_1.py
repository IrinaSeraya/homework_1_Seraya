import functools
import time

def timing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time_ms = (end_time - start_time) * 1000
        print(f"Время выполнения функции {func.__name__}: {execution_time_ms} мс")
        return result
    return wrapper

@timing
def test_function(n):
    time.sleep(n)
    return n * 3

result = test_function(0.2)
print(result)
