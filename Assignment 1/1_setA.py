'''
1 SET A
Generate the first prime number larger than a given natural number n.
'''
def read():
    n = int(input("Give the number n: "))
    return n

def isPrime(n):
    if(n < 2):
        return False;
    if(n > 2 and n % 2 == 0):
        return False;
    for i in range(3, n, 2):
        if(n % i == 0):
            return False
    return True

def printNumber(n,m):
    print("The first prime number larger than", n, "is", m)

def findFirstPrimeNumber(n):
    ok = False;
    i = n
    while(ok == False):
        i += 1
        if(isPrime(i)):
            ok = True
    return i

n = read()
printNumber(n, findFirstPrimeNumber(n))
