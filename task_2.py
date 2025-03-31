# Задание 2. 
user_string = input('Введите строку ')
user_string = user_string.lower()  #Делаем всю строку в нижнем регистре
user_string = user_string.replace('a', '') #Убираем гласную a
user_string = user_string.replace('i', '') #Убираем гласную i
user_string = user_string.replace('o', '') #Убираем гласную o
user_string = user_string.replace('u', '') #Убираем гласную u
user_string = user_string.replace('e', '') #Убираем гласную e
print('Строка без гласных ' + user_string)  #Вывод строки без гласных
