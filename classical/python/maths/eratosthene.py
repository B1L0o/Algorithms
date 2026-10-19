import math

def eratosthenes(n):
    primes = [x % 2 == 1 or x == 2 for x in range(n + 1)]
    root = math.ceil(math.sqrt(n))
    for i in range(3, root+1, 2):
        for j in range(i, n+1, i):
            if i != j:
                primes[j] = False
    return [i for i in range(n+1) if primes[i]]


if __name__ == "__main__":
    arg = int(input("choose a number: "))
    print(eratosthenes(arg))

