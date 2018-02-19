'''
For a given natural number n find the minimal natural number m formed with the same digits.
E.g. n=3658, m=3568.
'''

def read():
    x = (int(input("Give the number: ")))
    return x

def printNumber(a, x):
    print("the minimal natural number formed with the same digits of", a, "is" ,x)

def findDigits(x):
    digits= []
    for i in range (1,11):
        digits.append(0)
    while(x):
        digits[x%10] = digits[x%10] +1
        x = int(x/10)
    return digits

def createNumber(digits):
    x = 0
    i = 1
    if(digits[0]):
        while(digits[i] == 0):
            i = i+1
        x = x * 10 + i
        digits[i] -= 1
        for i in range (0, 10):
            while(digits[i]):
                x = x * 10 + i
                digits[i] -= 1
    else:
        for i in range (1, 10):
            while(digits[i]):
                x = x * 10 + i
                digits[i] -= 1
    return x
        
a = read()
printNumber(a, createNumber(findDigits(a)))
