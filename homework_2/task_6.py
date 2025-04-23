#Пользователь вводит список (любой). Удалите все дубликаты без использования set()
user_input = list(input('Введите список ').split())
unique_list = list(dict.fromkeys(user_input))
print('Список уникальных элементов ', unique_list)