'''
The numbers n1 and n2 have the property P if their writings in basis 10 have the same digits
(e.g. 2113 and 323121). Determine whether two given natural numbers have the property P.
'''

def readNumber():
    x = int(input("Give the number: "))
    return x
def printResult(x):
    if(x == True):
        print("The two numbers have the property P")
    else:
        print("The two numbers don't have the property P")

def determineDigits(x):
    digits= []
    for i in range (1,11):
        digits.append(0)
    while(x):
        digits[x%10] = 1
        x = int(x/10)
    return digits
def findProperty(x, y):
    l1 = determineDigits(x)
    l2 = determineDigits(y)
    for i in range (0, 10):
        if(l1[i] != l2[i]):
            return False
    return True
x = readNumber()
y = readNumber()
printResult(findProperty(x, y))
    
