# Stock management optimization - Maxsum

def kadane(arr):
    m = float("-inf")
    current = 0 

    for element in arr:
        current = max(element,element + current)
        m = max(m,current)

    return m
