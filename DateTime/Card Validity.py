import datetime

card1 = 20147
card2 = 54785
card3 = 85742
card4 = 54654

tday = datetime.datetime.now()

val1 = (tday - datetime.datetime(2019,3,31,12,0,0,0)).total_seconds()
val2 = (tday - datetime.datetime(2020,3,31,12,0,0,0)).total_seconds()
val3 = (tday - datetime.datetime(2020,4,1,17,0,0,0)).total_seconds()
val4 = (tday - datetime.datetime(2020,4,30,12,0,0,0)).total_seconds()




uCard = int(input("Enter Card Number"))

if uCard ==card1 and val1<0:
    print("Your card number :" + str(card1) +" is Valid as on " + str(datetime.date.today()) )
elif uCard ==card2 and val2<0:
    print("Your card number :" + str(card2) +" is Valid as on " + str(datetime.date.today()) )
elif uCard ==card3 and val3<0:
    print("Your card number :" + str(card3) +" is Valid as on " + str(datetime.date.today()) )
elif uCard ==card4 and val4<0:
    print("Your card number :" + str(card4) +" is Valid as on " + str(datetime.date.today()) )
else:
    print("Your card number :" + str(uCard) +" is Invalid as on " + str(datetime.date.today()) )
