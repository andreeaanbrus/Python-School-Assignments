import copy


def readNumber():
    x = int(input("Give the number"))
    return x


def findPrime(x):
    """

    :param x: the given number
    :return: the list of prime numbers until the number x
    """
    prime = []
    for i in range(0, x + 1):
        if isPrime(i):
            prime.append(i)
    return prime


def isPrime(x):
    """
    checks if x is prime
    :param x: the given number
    :return: True if x is prime
            False otherwise
    """
    if x < 2:
        return False
    if x % 2 == 0 and x > 2:
        return False
    for d in range(3, int(x / 2)):
        if x % d == 0:
            return False
    return True


def back(number):
    """
    find all possible decompositions as sums of prime numbers
    """
    primes = findPrime(number)
    def recursive(curList):
        if sum(curList) == number:
            print("result: ", curList)
            return
        if sum(curList) > number:
            return
        for i in primes:
            curList.append(i)
            recursive(copy.deepcopy(curList))
            curList = curList[:-1]

    def nonrecursive(curList):
        backQueue = [curList]
        while len(backQueue) != 0:
            curList = backQueue[0]
            backQueue = backQueue[1:]
            if sum(curList) == number:
                print("result: ", curList)
            elif sum(curList) < number:
                for i in primes:
                    curList.append(i)
                    if sum(curList) <= number:
                        backQueue.append(curList)
                    curList = curList[:-1]
    print("recursive")

    recursive([])
    print("nonrecursive")
    nonrecursive([])


def main():
    x = readNumber()
    back(x)


main()
