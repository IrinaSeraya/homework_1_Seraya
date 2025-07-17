import time
import functools

def wam_if_slow(seconds):
    def decorator(func):
        @functools.wraps(func)
        def wrapper (*args, **kwargs):
            start_time = time.time()
            result = func (*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            if execution_time > seconds:
                print(f"Функция {func.__name__} выполнялась {execution_time}, что дольше {seconds} секунд")
            return result
        return wrapper
    return decorator

#Testing
@wam_if_slow(2)
def test_function(a):
    time.sleep(a)
    return "Выполнено"

print(test_function(3))