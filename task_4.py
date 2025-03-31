user_password = input ('Введите пароль ')
alphabets = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
l, u = 0, 0
if (len(user_password) <= 16):
    print ('Слишком короткий пароль')
else:
    for i in user_password:
        if (i in alphabets):
            l +=1
        if (i in digits):
            u +=1
    if (l<1 or u<1 and l+u== len(user_password)):
         print('Слабый пароль')
    else:
         print ('Надежный пароль')
