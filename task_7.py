user_input = int(input('Введите количество секунд '))
minutes = user_input // 60
seconds = user_input % 60
print(str(minutes) + ' минут(-а) и ' + str(seconds) + ' секунд(-а)') 
#Не уверена, надо ли было выводить количество секунд, если кол-во градусов не кратно 6