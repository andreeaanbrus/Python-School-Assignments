'''
For a given natural number n find the largest natural number m formed with the same digits.
E.g. n=3658, m=3568.
'''

def read():
    x = (int(input("Give the number: ")))
    return x

def printNumber(a, x):
    print("The largest natural number formed with the same digits of", a, "is" ,x)

def findDigits(x):
    digits= []
    while(x):
        digits.append(x % 10)
        x = int(x/10)
    digits.sort(reverse = True)
    return digits

def createNumber(digits):
    x = 0
    p = 1
    for i in digits:
        x = x * 10 +i
    return x
a = read()
printNumber(a, createNumber(findDigits(a)))
