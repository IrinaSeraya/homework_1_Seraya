users_amount_of_money = int(input('Введите сумму денег '))
nominal_100 = users_amount_of_money // 100
nominal_50 = (users_amount_of_money - nominal_100*100) //50
nominal_20 = (users_amount_of_money - nominal_100*100 - nominal_50*50) // 20
nominal_10 = (users_amount_of_money - nominal_100*100 - nominal_50*50 - nominal_20*20) //10
nominal_5 = (users_amount_of_money - nominal_100*100 - nominal_50*50 - nominal_20*20 - nominal_10*10) // 5
nominal_2 = (users_amount_of_money - nominal_100*100 - nominal_50*50 - nominal_20*20 - nominal_10*10 - nominal_5*5) // 2
nominal_1 = (users_amount_of_money - nominal_100*100 - nominal_50*50 - nominal_20*20 - nominal_10*10 - nominal_5*5 - nominal_2*2) //1
print(str(nominal_100) + ' купюр(-a) по 100р \n' + str(nominal_50) + ' купюр(-a) по 50р \n' 
      + str(nominal_20) + ' купюр(-a) по 20р \n' + str(nominal_10) + ' купюр(-a) по 10р \n'
     + str(nominal_5) + ' купюр(-a) по 5р \n' + str(nominal_2) + ' монет(-a) по 2р \n' 
      + str(nominal_1) + ' монет(-a) по 1р \n' )