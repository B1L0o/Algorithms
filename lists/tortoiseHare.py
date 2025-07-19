# Works the same with linked lists

def findDuplicates(arr):
    tortoise = arr[0]
    hare = arr[0]

    tortoise = arr[tortoise]
    hare = arr[arr[hare]]
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]

    tortoise = arr[0]
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]

    return tortoise

if __name__ == "__main__":
    print(findDuplicates([1,2,  3,4,5,2,6,7,8,9]))
