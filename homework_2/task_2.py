# Пользователь вводит список чисел. Числа вводятся через пробел, могут быть как целые, так и с плавающей точкой. Выведите на экран:
#1. Уникальные числа.
#2. Повторяющиеся числа.
#3. Четные и нечетные чисел.
#4. Отрицательные чисел.
#5. Числа с плавающей точкой.
#6. Сумму всех чисел, кратных 5.
#7. Самое большое число.
#8. Самое маленькое число.
user_input = input('Введите числа ').split()
lst_of_numbers = list(user_input)
unique_numbers = []

for unique in lst_of_numbers:
   count_unique = lst_of_numbers.count(unique)
   if count_unique == 1:
      unique_numbers.append(unique)

same_numbers = set(lst_of_numbers) - set(unique_numbers)

positive_numbers = set()
negative_numbers = set()
for p_number in unique_numbers:
   if float(p_number) > 0:
      positive_numbers.add(p_number)
   else:
      negative_numbers.add(p_number)
for p_number in same_numbers:
   if float(p_number) > 0:
      positive_numbers.add(p_number)
   else:
      negative_numbers.add(p_number)  

float_numbers = set()
for number_float in unique_numbers:
   if float(number_float) - float(number_float)//1 > 0:
      float_numbers.add(number_float)
for number_float in same_numbers:
   if float(number_float) - float(number_float)//1 > 0:
      float_numbers.add(number_float)
int_numbers = (set(unique_numbers) - float_numbers) | (same_numbers - float_numbers)

even_numbers = set()
odd_numbers = set()
for number in positive_numbers:
   if float(number) % 2 == 0:
      even_numbers.add(number)
   if float(number) % 2 == 1:
      odd_numbers.add(number)   
for number in positive_numbers:
   if float(number) % 2 == 0:
      even_numbers.add(number)
   if float(number) % 2 == 1:
      odd_numbers.add(number)

sum_numbers_div_five = 0
for num_div_five in lst_of_numbers:
   if float(num_div_five) % 5 == 0:
      sum_numbers_div_five = sum_numbers_div_five + float(num_div_five)

max_number = float(lst_of_numbers[0]) #ошибка
for num_max in lst_of_numbers:
   if float(num_max) > max_number:
      max_number = float(num_max)

min_number = float(lst_of_numbers[0]) #ошибка
for num_min in lst_of_numbers:
   if float(num_min) < min_number:
      min_number = float(num_min)

print('Вы ввели: ' + str(lst_of_numbers))
print('1. Уникальные числа: ' + str(unique_numbers))
print('2. Повторяющиеся числа: ' + str(same_numbers))
print('3. Четные числа ' + str(even_numbers) + ' и нечетные числа ' + str(odd_numbers))
print('4. Отрицательные числа ' + str(negative_numbers))
print('5. Числа с плавающей точкой ' + str(float_numbers))
print('6. Сумма чисел кратных 5 ' + str(sum_numbers_div_five))
print('7. Самое большое число ' + str(max_number))
print('8. Самое маленькое число ' + str(min_number))