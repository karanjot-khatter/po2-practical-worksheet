#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     22/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
def circumferenceOfCircle():
    radius = eval(input("Please enter the radius of a circle"))
    circumfererence = 2 * math.pi * radius
    print("The circumference of the radius, ", round(radius,2), "is:", round(circumfererence,2))

circumferenceOfCircle()

def areaOfCircle():

    radius = eval(input("Please enter the radius of a circle"))
    area = math.pi * (radius ** 2)
    print("The area of the radius", round(radius,2), "is:", round(area,2))
areaOfCircle()

def costOfPrizza():
    diameter = eval(input("Please enter the diamater of a pizza (in cm)"))
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    cost = (area / 1.5) * 100
    print("The cost of the pizza's ingrediants is:",round(cost,2), "pence")

costOfPrizza()

def slopeOfLine():

    x1,y1 = eval(input("Please enter the 2 values for x1 and y1 (x1,y1)"))
    x2,y2 = eval(input("Please enter the 2 values for x1 and y1 (x2,y2)"))
    slope = (y2 - y1) / (x2 - x1)
    print("The slope of the line that connects them is", slope)
slopeOfLine()

def distanceBetweenPoints():
    x1,y1 = eval(input("Please enter the 2 values for x1 and y1 (x1,y1)"))
    x2,y2 = eval(input("Please enter the 2 values for x1 and y1 (x2,y2)"))
    distance =((x2-x1)**2) + ((y2-y1) **2)
    sqrt = math.sqrt(distance)
    print("The distance between the points is:", sqrt)
distanceBetweenPoints()

def travelStatistics():

    speed,duration = (eval(input("Please enter the average speed (in km/hour) and duration (in hours) of a car journey (speed,duration)")))
    overalDistanceTravelled = speed * duration
    amountOfFuelUsed = overalDistanceTravelled / 5
    print("The overal distance travelled is,", overalDistanceTravelled, "km. The amount of fuel used is:", amountOfFuelUsed, "litres")
travelStatistics()

def sumOfNumbers():
    print("This program outputs the sum of the ifrst n positive numbers")
    n = eval(input("Please enter how many numbers need entering"))
    sum = n * (n+1) / 2
    print("The sum of the", n, "positive intergers is",sum)

sumOfNumbers()

def averageofNumbers():
    inputted = eval(input("Please enter the amount of numbers to be there are to be inputted?"))
    sum = 0
    for i in range(inputted):
        i = eval(input("Please enter a number: "))
        sum = sum + i

    print(sum / inputted) #float
averageofNumbers()

def selectCoins():
    money = eval(input("Please enter the amount of money in (pence):"))
    print("This program outputs the number of coins of each denomination, making the exact change of:", money)
    bank = money

    if bank >= 200:
        twoPound =bank // 200
        bank = bank - (twoPound * 200)
        print (twoPound, "* Â£2")
    else:
        print("0 * Â£2")

    if bank >= 100:
        onePound = bank // 100
        bank = bank - (onePound * 100)
        print (onePound, "* Â£1")
    else:
        print("0 * Â£1")

    if bank >= 50:
        fifty = bank // 50
        bank = bank - (fifty * 50)
        print (fifty, "* Â£0.50")
    else:
        print("0 * Â£0.50")

    if bank >= 20:
         twen = bank // 20
         bank = bank - (twen * 20)
         print (twen, "* Â£0.20")
    else:
        print("0 * Â£0.20")

    if bank >= 10:
        ten = bank // 10
        bank = bank - (ten * 10)
        print (ten, "* Â£0.10")

    else:
        print("0 * Â£0.10")

    if bank >= 5:
        five = bank // 5
        bank = (five, "* Â£0.05")

    else:
        print("0 * Â£0.05")

    if bank >= 2:
        two = bank // 2
        bank = bank - (two * 2)
        print (two, "* Â£0.02")

    else:
        print("0 * Â£0.02")

    if bank >= 1:
        one = bank // 1
        bank = bank - (one * 1)
        print (one, "* Â£0.01")

    else:
        print("0 * Â£0.01")

selectCoins()