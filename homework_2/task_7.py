#Пользователь вводит строку. Напишите программу, которая сжимает строку следующим образом: 
# если символ X повторяется N раз, то итоговая строка должна содержать XN.
user_input = input('Введите строку ')
shorter_string = ''
for char in user_input:
    if user_input.count(char) >= 2 and char not in shorter_string:
        shorter_string += char + str(user_input.count(char))
    elif char not in shorter_string:
        shorter_string += char
print('Сжатая строка ', shorter_string)