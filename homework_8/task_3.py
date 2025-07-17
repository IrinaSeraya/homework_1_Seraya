import functools


def type_check(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
        for i, arg_name in enumerate(arg_names):
            if arg_name in annotations:
               expected_type = annotations[arg_name]
               if i < len(args):
                  actual_type = type(args[i])
                  if actual_type is not expected_type:
                     raise TypeError(f"Ожидался аргумент типа {expected_type.__name__} для {arg_name}, получен {actual_type.__name__}")
               elif arg_name in kwargs:
                  actual_type = type(kwargs[arg_name])
                  if actual_type is not expected_type:
                     raise TypeError(f"Ожидался аргумент типа {expected_type.__name__} для {arg_name}, получен {actual_type.__name__}")
               else:
                  print("Аргумент не передан") 
        return func(*args, **kwargs)
    return wrapper
   
@type_check
def add(a: int, b: int):
   return a + b

print(add(6, 10))
print(add('f', 5))
