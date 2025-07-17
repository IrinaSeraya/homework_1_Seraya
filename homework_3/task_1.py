#Напишите функцию, которая принимает список и делает его “плоским”. 
# Используйте рекурсию. Функция должна модифицировать переданный список, а не создавать новый.
#Первый вариант
def flatten_list (lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result
#Второй вариант
def flatten(lt):
    if not lt:
        return []
    if isinstance(lt[0], list):
        return flatten(lt[0]) + flatten(lt[1:])
    return lt[:1] + flatten(lt[1:])
spis = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
print(flatten_list(spis))
print(flatten(spis))