'''
The palindrome of a number is the number obtained by reversing the order of digits. E.g.
palindrome (237) = 732). For a given natural number n, determine its palindrome.
'''

def read():
    x = int(input("Give the number: "))
    return x

def printPalindrome(x, y):
    print("The palindrome of" , x, "is" , y)

def mirrored(x):
    m = 0
    y = x
    while(y):
        m = m * 10 + y % 10
        y = int(y/10)
    return m

x = read()
printPalindrome(x, mirrored(x))
