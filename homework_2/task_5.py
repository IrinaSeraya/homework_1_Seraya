#Пользователь вводит 2 слова. Напишите программу, которая проверяет, являются ли они анаграммами 
#(первое слово может быть сформировано путем перестановки букв во втором слове)
user_input_1 = (input('Введите первое слово '))
user_input_2 = (input('Введите второе слово '))
set_of_symbols_1 = set(user_input_1)
set_of_symbols_2 = set(user_input_2)
if len(user_input_1) == len(user_input_2) and set_of_symbols_1 == set_of_symbols_2:
     print('Слова ', user_input_1, ' и ', user_input_2, ' являются анаграммами')
else:
    print('Слова ', user_input_1, ' и ', user_input_2, ' не являются анаграммами')