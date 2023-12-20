import math
print("Welcome to Jason's Cafe! Please select one of the following options.") #Welcome message for user
print("--------------------------------------------------------------------")

SMALL_CUP_SIZE = 9  # Creating Constants for cup sizes and costs
MEDIUM_CUP_SIZE = 12
LARGE_CUP_SIZE = 15
SMALL_CUP_PRICE = 1.75
MEDIUM_CUP_PRICE = 1.90
LARGE_CUP_PRICE = 2.00

def menu():  # Print menu function that provides customer with different options
    print("1: Enter 1 to order coffee.")
    print("2: Enter 2 to check the total money made up to this time.")
    print("3: Enter 3 to check the total amount of coffee sold up to this time.")
    print("4: Enter 4 to check the number of cups of coffee of each size sold.")
    print("5: Enter 5 to print the data.")
    print("9: Enter 9 to exit the program.")

def orderCoffee(smallCupCount, mediumCupCount, largeCupCount, coffeeSold, moneyMade):
    print("1: Enter 1 to buy coffee in a small cup size (9 oz)")
    print("2: Enter 2 to buy coffee in a medium cup size (12 oz)")
    print("3: Enter 3 to buy coffee in a large cup size (15 oz)")
    print("9: Enter 9 to exit.")
    option = int(input())

    cups = 0
    if option in {1, 2, 3}:
        cups = int(input("Enter the number of cups: "))

    if option == 1:
        smallCupCount += cups
        coffeeSold += cups * SMALL_CUP_SIZE
        moneyMade += cups * SMALL_CUP_PRICE
    elif option == 2:
        mediumCupCount += cups
        coffeeSold += cups * MEDIUM_CUP_SIZE
        moneyMade += cups * MEDIUM_CUP_PRICE
    elif option == 3:
        largeCupCount += cups
        coffeeSold += cups * LARGE_CUP_SIZE
        moneyMade += cups * LARGE_CUP_PRICE
    elif option == 9:
        print(f"Please pay ${moneyMade:.2f}")

    return smallCupCount, mediumCupCount, largeCupCount, coffeeSold, moneyMade

def totalMoneyMade(moneyMade):  # Creating function for Option #2 total amount of money made
    print(f"Total money made: ${moneyMade:.2f}")

def totalCoffeeSold(coffeeSold): # Creating function for Option #3 for total amount of coffee sold
    print(f"Total amount of coffee sold: {coffeeSold} oz")

def numOfCups(smallCupCount, mediumCupCount, largeCupCount):  # Function for Option #4 to check the number of cups of coffee of each size sold
    print(f"Small cup count: {smallCupCount}")
    print(f"Medium cup count: {mediumCupCount}")
    print(f"Large cup count: {largeCupCount}")

def printData(smallCupCount, mediumCupCount, largeCupCount, coffeeSold, moneyMade): # Function for Option #5 Print Data
    numOfCups(smallCupCount, mediumCupCount, largeCupCount)
    totalCoffeeSold(coffeeSold)
    totalMoneyMade(moneyMade)

def main():
    smallCupCount = 0  # Creating variables for cup counts and money made
    mediumCupCount = 0
    largeCupCount = 0
    coffeeSold = 0
    moneyMade = 0
    while True:  # While loop with if else statements to drive the main program
        menu()
        option = int(input())
        if option == 1:
            smallCupCount, mediumCupCount, largeCupCount, coffeeSold, moneyMade = orderCoffee(
            smallCupCount, mediumCupCount, largeCupCount, coffeeSold, moneyMade
        )
        elif option == 2:
            totalMoneyMade(moneyMade)
        elif option == 3:
            totalCoffeeSold(coffeeSold)
        elif option == 4:
            numOfCups(smallCupCount, mediumCupCount, largeCupCount)
        elif option == 5:
            printData(smallCupCount, mediumCupCount, largeCupCount, coffeeSold, moneyMade)
        elif option == 9:
            break
        else:
            print(" Error!! Invalid Input. Please select a valid option (1/2/3/4/5/9).")
main()