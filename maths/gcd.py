def gcd(a,b):
    return a if b==0 else gcd(b,a%b)

if __name__ == "__main__":
    a = int(input("choose a first number: "))
    b = int(input("choose a second number: "))
    print(gcd(a,b))