ip_adress = input('Введите IP-адрес ').split('.')
for i in ip_adress:
    if not (0 <= int(i) <= 255):
        print ('Некорректный IP-адрес')
        break
else:
    print('Корректный IP-адрес')