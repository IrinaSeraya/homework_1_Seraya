#Пользователь вводит список чисел. Найдите второе по величине число
user_input = list(map(int, input('Введите список чисел ').split()))
user_input.sort()
print('Второе по величине число ', user_input[-2])