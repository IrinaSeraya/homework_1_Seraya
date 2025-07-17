import functools

def retry(exceptions, n):
    def retry_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            tries = n
            while tries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    tries -= 1
                    if not tries:
                        raise e
        return wrapper
    return retry_decorator

@retry(ValueError, n=2)
def test_func():
    a = int(input("Введите число "))
    print(a)

test_func()
