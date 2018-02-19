'''
Generate the largest perfect number smaller than a given natural number n. If such a number
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

def largestPerfectNumber(x):
    ok = False
    i = x
    while(not ok and i):
        i -= 1
        if(isPerfect(i)):
            ok = True
    if(i == 0):
        return False
    else:
        return i

def printNumber(n,x):
    if(x == False):
        print("The largest perfect number smaller than", n, "doesn't exist")
    else:
        print("The largest perfect number smaller than", n, "is", x)

n = read()
printNumber(n,largestPerfectNumber(n))
