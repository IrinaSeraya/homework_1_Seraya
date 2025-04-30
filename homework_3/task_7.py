# Реализуйте функцию merge_sorted_list, которая принимает два отсортированных списка, 
# и возвращает новый отсортированный список, содержащий элементы из обоих списков.
from heapq import merge
def merge_sorted_list (list_1, list_2):
    merge_sorted_list = []
    for i in list_1:
        for j in list_2:
            if i == j:
                merge_sorted_list.append(i)
    return merge_sorted_list
    #merge_sorted_list = merge (list_1.sort(), list_2.sort())

spis_1 = list(input('Введите первый список').split())
spis_2 = list(input('Введите второй список').split())
new_merge_sorted_list = merge_sorted_list(spis_1, spis_2)
print(new_merge_sorted_list)