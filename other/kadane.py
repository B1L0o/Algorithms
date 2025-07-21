# Stock management optimization - Maximum sum in an array

def kadane(arr):
    m = float("-inf")
    current = 0 

    for element in arr:
        current = max(element,element + current)
        m = max(m,current)

    return m

if __name__ == "__main__":
    array = [1,2,-3,4,3,-4,-2,1]
    print(kadane(array))