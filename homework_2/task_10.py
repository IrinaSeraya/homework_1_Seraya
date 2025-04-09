#Найдите самую длинную подстроку без дубликатов
user_input = input('Введите строку ')
short_version = ''
for char in user_input:
     if char not in short_version:
        short_version += char
print('Сжатая строка ', short_version)