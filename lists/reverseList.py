class Node:
    def __init__(self, val=0, Next=None):
        self.val=val
        self.next=Next

def reverse(head):
    curr=head
    prev=None
    while curr:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev

def printNode(head):
    curr=head
    while curr:
        print(curr.val)
        curr=curr.next


if __name__ == "__main__":
    head=Node(1,None)
    e1=Node(2,None)
    e2=Node(3,None)
    e3=Node(4,None)

    head.next=e1
    e1.next=e2
    e2.next=e3

    printNode(head)
    print()
    head = reverse(head)
    print()
    printNode(head)
