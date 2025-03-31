alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter = input('Введите букву ')
shift = int(input('Сдвиг на '))
result = ''
for c in letter:
    result += alphabet[(alphabet.index(c) + shift) % len (alphabet)]
print ('Итог:'+ result)