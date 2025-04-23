# Реализуйте функцию merge_sorted_list, которая принимает два отсортированных списка, и возвращает новый отсортированный список, содержащий элементы из обоих списков.
from heapq import merge
def merge_sorted_list (list_1, list_2):
    return sorted(list_1 + list_2)
    #merge_sorted_list = merge (list_1.sort(), list_2.sort())

spis_1 = list(input().split())
spis_2 = list(input().split())
new_merge_sorted_list = merge_sorted_list(spis_1, spis_2)
print(new_merge_sorted_list)

def unique_elements(lst):
    unique_list = []
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
print(unique_elements(new_merge_sorted_list))