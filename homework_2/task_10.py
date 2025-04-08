#Найдите самую длинную подстроку без дубликатов
user_input = input('Введите строку ')
short_version = ''
for char in user_input:
 #   if user_input.count(char) >= 2 and char not in shorter_string:
  #      shorter_string += char + str(user_input.count(char))
    if char not in short_version:
        short_version += char
print('Сжатая строка ', short_version)