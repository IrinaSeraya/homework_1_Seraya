# Напишите функцию unique_elements, которая принимает вложенный список и возвращает уникальные элементы.
from functools import  wraps
    
def flatten_list (lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result
spis = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]
input_list = flatten_list(spis)

def unique_elements(lst):
    unique_list = []
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


print(unique_elements(input_list))
#input_list = []
#input_list.append(list(map(int, input().split())))
#print(unique_elements(input_list))