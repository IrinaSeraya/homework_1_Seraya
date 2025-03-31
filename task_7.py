user_input = int(input('Введите количество секунд '))
minutes = user_input // 60 #Кол-во минут
seconds = user_input % 60 #Кол-во секунд
print(str(minutes) + ' минут(-а) и ' + str(seconds) + ' секунд(-а)') 