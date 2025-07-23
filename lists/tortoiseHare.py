# Given an array of integers nums containing n + 1 where each integer is in the range [1, n] inclusive. 
# There is only one repeated number in nums, return this repeated number.
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


# Detects cycle in a linked list
def detectCycle(head):
    slow = head.next
    fast = head.next.next 

    while slow.val != fast.val:
        slow = slow.next 
        fast = fast.next.next 

    slow = head 
    while slow.val != fast.val:
        slow  = slow.next 
        fast = fast.next 
    
    return slow.val


if __name__ == "__main__":
    print(findDuplicates([1,2,  3,4,5,2,6,7,8,9]))
