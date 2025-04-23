#Программа случайно загадывает число от 1 до 100.
#● Пользователь вводит догадки.
#● Программа подсказывает "Больше" или "Меньше".
#● Игра продолжается, пока пользователь не угадает.
from random import randint
secret_number = randint(1, 100)
print('')
user_number = 0
try_count = 0
while user_number != secret_number:
    try_count += 1
    user_number = int(input(f'{try_count}-я попытка: '))
    if user_number > secret_number:
        print('Меньше')
    elif user_number < secret_number:
        print('Больше')
    else:
        print(f'Правильно. Загадано число {secret_number}')