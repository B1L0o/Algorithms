from linkedLists import List

def reverse(head):
    curr=head
    prev=None
    while curr:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    return prev

if __name__ == "__main__":
    l = List()
    l.add_back(1)
    l.add_back(2)
    l.add_back(3)
    l.add_back(4)
    l.dump()
    print()
    l.head = reverse(l.head)
    l.dump()
