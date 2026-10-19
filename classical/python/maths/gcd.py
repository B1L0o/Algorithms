def gcd(a,b):
    return a if b==0 else gcd(b,a%b)

if __name__ == "__main__":
    a = int(input("choose a first number:\n"))
    b = int(input("choose a second number:\n"))
    print(gcd(a,b))