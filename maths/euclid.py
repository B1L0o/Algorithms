def euclid(a,b):
    if a == 0:
        return b,0,1
    gcd,x1,y1 = euclid(b%a,a)
    x = y1 - (b//a) * x1
    y = x1 
    return gcd,x,y

if __name__ == "__main__":
    a = int(input("choose a first number: "))
    b = int(input("choose a second number: "))
    gcd, x, y = euclid(a, b)
    print(f"GCD: {gcd}, x: {x}, y: {y}")