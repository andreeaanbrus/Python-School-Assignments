'''
Generate the larges prime number smaller than a given natural number n. If such a number
does not exist, a message should be displayed.

'''

def read():
    x = int(input("Give the number: "))
    return x

def printNumber(n,x):
    if(largestPrimeNumber(x) == False):
        print("The largest prime number smaller than the given number does not exist!")
    else:
        print ("The largest prime number smaller than",n,"is",x)

def isPrime(x):
    if(x < 2):
        return False
    if(x > 2 and x % 2 == 0):
        return False
    for d in range(3, x, 2):
        if( x % d == 0):
            return False
    return True

def largestPrimeNumber(x):
    for i in range(x-1, 1, -1):
        if(isPrime(i)):
            return i
    return False

n = read()
printNumber(n,largestPrimeNumber(n))
