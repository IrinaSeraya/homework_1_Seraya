#Напишите функцию, которая производит слияние двух словарей. Используйте рекурсию.
#В обоих словарях может быть любой уровень вложенности. 
#Вложены могут быть другие коллекции: словари, списки, множества, кортежи.
def merge_dicts (dict_1, dict_2):
    for a, b in dict_2.items():
        if a in dict_1 and isinstance(dict_1[a], dict) and isinstance(b, dict):
            merge_dicts(dict_1[a], b)
        else:
            dict_1[a] = b
    return dict_1

dict_a = {'a': 1, 'b': {'c': 1, 'f': 4}}
dict_b = {'d': 1, 'b': {'c': 2, 'e': 3}}
merge_dicts(dict_a, dict_b)
print(dict_a)
