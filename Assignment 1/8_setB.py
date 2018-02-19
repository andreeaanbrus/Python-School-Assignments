'''
Determine the twin prime numbers p1 and p2 immediately larger than the given non-null
natural number n. Two prime numbers p and q are called twin if q-p = 2.
'''
def read():
    x = int(input("Give the number: "))
    return x

def isPrime(x):
    if(x < 2):
        return False
    if(x > 2 and x % 2 == 0):
        return False
    for d in range(3, int(x / 2), 2):
        if(x % d == 0):
            return False
    return True

def twin(x, y):
    if(y - x == 2):
        return True
    return False

def printNumbers(a, p1):
    print("The twin prime numbers immediately larger than the given number",a,"are", p1)

def determineTwinPrimeNumbers(x):
    n = x + 1
    ok = False
    while(not ok):
        if(isPrime(n) and isPrime(n + 2)):
            return (n, n+2)
        n = n + 1

a = read()
printNumbers(a, determineTwinPrimeNumbers(a))
