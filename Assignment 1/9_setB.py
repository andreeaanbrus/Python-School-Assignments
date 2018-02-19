'''
Find the smallest number m from the Fibonacci sequence, defined by f[0]=f[1]=1, f[n]=f[n-
1]+f[n-2], for n>2, larger than the given natural number n. So, find k and m such that f[k]=m,
m>n and f[k-1] <=n.
'''

def read():
    n = int(input("Give the number: "))
    return n


def fibo(n):
    f0 = 1
    f1 = 1
    fk = f0 + f1
    pos = 2
    while(fk <= n):
        fk = f0 + f1
        f0 = f1
        f1 = fk
        pos += 1
    return (fk, pos)     
def printNumbers(n):
    print("The number m is" , n[0])
    print("Its position in Fibonacci sequence is ", n[1])
x = read()
printNumbers(fibo(x))
