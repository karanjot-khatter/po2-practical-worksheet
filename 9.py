#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     25/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def selectCoins():
    money = eval(input("Please enter the amount of money in (pence):"))
    print("This program outputs the number of coins of each denomination, making the exact change of:", money)
    bank = money

    if bank >= 200:
        twoPound =bank // 200
        bank = bank - (twoPound * 200)
        print (twoPound, "* £2")
    else:
        print("0 * £2")

    if bank >= 100:
        onePound = bank // 100
        bank = bank - (onePound * 100)
        print (onePound, "* £1")
    else:
        print("0 * £1")

    if bank >= 50:
        fifty = bank // 50
        bank = bank - (fifty * 50)
        print (fifty, "* £0.50")
    else:
        print("0 * £0.50")

    if bank >= 20:
         twen = bank // 20
         bank = bank - (twen * 20)
         print (twen, "* £0.20")
    else:
        print("0 * £0.20")

    if bank >= 10:
        ten = bank // 10
        bank = bank - (ten * 10)
        print (ten, "* £0.10")

    else:
        print("0 * £0.10")

    if bank >= 5:
        five = bank // 5
        bank = (five, "* £0.05")

    else:
        print("0 * £0.05")

    if bank >= 2:
        two = bank // 2
        bank = bank - (two * 2)
        print (two, "* £0.02")

    else:
        print("0 * £0.02")

    if bank >= 1:
        one = bank // 1
        bank = bank - (one * 1)
        print (one, "* £0.01")

    else:
        print("0 * £0.01")

selectCoins()