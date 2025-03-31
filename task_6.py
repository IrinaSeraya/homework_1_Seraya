user_input = int(input('Введите число '))
sum = 0
remains = user_input % 7 #Остаток от деления на 7
if (remains == 0 ):
    print('Магическое число')
else:
    while user_input > 0:           #Считаем сумму цифр
        sum += user_input % 10
        user_input = user_input // 10
    print(sum)