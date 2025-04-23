#Пользователь вводит строку. Напишите программу, которая сжимает строку следующим образом: 
# если символ X повторяется N раз, то итоговая строка должна содержать XN.
user_input = input('Введите строку ')
shorter_string = ''
first_symbol = user_input[0]
count_of_symbol = 1
for char in range(len(user_input) - 1):
    next_symbol = user_input[char+1]
    if next_symbol == first_symbol:
        count_of_symbol += 1
    else:
        shorter_string += first_symbol + str(count_of_symbol)
        count_of_symbol = 1
    first_symbol = next_symbol
shorter_string += first_symbol + str(count_of_symbol)
print('Сжатая строка ', shorter_string)