def getMap(s):
    m = {}
    n=len(s)
    for i in range(n-1):
        m[s[i]] = n-i-1
    return m 

def boyermoore(s,pattern):
    d = getMap(pattern)
    right,n = len(s),len(pattern)
    left = n-1 
    while left < right:
        valid=True
        for i in range(n-1):
            if s[left-i] != pattern[n-i-1]:
                valid = False
                break

        if valid:
            return True
        if s[left] in d.keys():
            left += d[s[left]]
        else:
            left += n
    return False

if __name__ == "__main__":
    s = input("Enter a sentence: \n")
    t = input("Enter a pattern: \n")
    print(f"'{t}' is present in '{s}'." if boyermoore(s,t) else f"'{t}' is not present in '{s}'.")