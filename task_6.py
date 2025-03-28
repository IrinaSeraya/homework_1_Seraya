user_input = int(input('Введите число '))
sum = 0
while user_input > 0:
    sum += user_input % 10
    user_input = user_input // 10
print(sum)