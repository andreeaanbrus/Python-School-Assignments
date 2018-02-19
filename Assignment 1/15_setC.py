'''
Generate the smallest perfect number larger than a given natural number n. If such a number
does not exist, a message should be displayed. A number is perfect if it is equal to the sum of its
divisors, except itself. E.g. 6 is a perfect number (6=1+2+3).
'''
def read():
    x = int(input("Give the number: "))
    return x

def isPerfect(x):
    s = 0
    n = int(x/2) + 1 
    for d in range(1, n):
        if(x % d == 0):
            s += d
    if(s == x):
        return True
    else:
        return False

def smallestPerfectNumber(x):
    ok = False
    i = x
    while(not ok):
        i += 1
        if(isPerfect(i)):
            ok = True
    return i

def printNumber(n,x):
    print("The smallest perfect number larger than", n, "is", x)

n = read()
printNumber(n,smallestPerfectNumber(n))
