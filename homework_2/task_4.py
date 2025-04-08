#Пользователь вводит 2 набора чисел. Выведите на экран:
#1. Числа, которые присутствуют в обоих наборах одновременно.
#2. Числа из первого набора, которые отсутствуют во втором, и наоборот.
#3. Числа из обоих наборов, за исключением чисел, найденных в пункте 1.
user_input_1 = set(map(int, input('Введите первый список чисел ').split()))
user_input_2 = set(map(int, input('Введите второй список чисел ').split()))
intersection = user_input_1 & user_input_2
print('Числа, которые присутствуют в обоих наборах одновременно ', intersection)
difference_1_2 = user_input_1 - user_input_2
print('Числа из первого набора, которые отсутствуют во втором ', difference_1_2)
difference_2_1 = user_input_2 - user_input_1
print('Числа из второго набора, которые отсутствуют в первом ', difference_2_1)
symmetric_difference = user_input_1 ^ user_input_2
print('Числа из обоих наборов, за исключением одинаковы чисел ', symmetric_difference)