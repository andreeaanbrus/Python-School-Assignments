'''
Determine the age of a person, in number of days
'''

def read():
    x = int(input("Give the age of a person "))
    return x

def determineNumberOfDays(x):
    y = 365 * x
    return y

def printNumberOfDays(x):
    print("The number of days is" , x)

n = read()
printNumberOfDays(determineNumberOfDays(n))
