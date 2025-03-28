user_input = input('Введите строку ')
palindrom = user_input[::-1]
if palindrom == user_input:
    print(str(user_input) + ' является палиндромом')
else:
    print('Введенная Вами строка "' + str(user_input) + '" не является палиндромом')