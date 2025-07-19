def getMap(s):
    m = {}
    n=len(s)
    for i in range(n-1):
        m[s[i]] = n-i-1
    return m 

def boyermoore(s,pattern):
    d = getMap(pattern)
    m,n = len(s),len(pattern)
    left = n-1 
    while left < m:
        valid=True
        for i in range(n-1):
            if s[left-i] != pattern[n-i-1]:
                valid = False

        if valid:
            return True
        if s[i] in d.keys():
            i += d[s[i]]
        else:
            i += n
    return False



if __name__ == "__main__":
    m = getMap("latroc")
    print(m)