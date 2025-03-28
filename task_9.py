number_1 = float(input('Введите первое дробное число '))
number_2 = float(input('Введите второе дробное число '))
if abs(number_1 - number_2) < 0.001:
    print('True')
else:
    print('False')