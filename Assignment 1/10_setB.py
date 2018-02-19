'''
10 SET B    
Consider a given natural number n. Determine the product p of all the proper factors of n.

'''

def read():
    x = int(input("Give the number: "))
    return x

def printProduct(x,p):
    print("The product of all the proper factors of" , x,"is",  p)
    
def determineProduct(n):
    p = 1
    x = int(n/2)
    for i in range(1, x + 1):
        if(n % i == 0):
            p *= i
    return p

x = read()
printProduct(x,determineProduct(x))
