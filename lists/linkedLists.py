from node import Node

class LinkedList:

    def __init__(self):
        self.head = None


    def length(self):
        res=0
        current = self.head 
        while current:
            current=current.next 
            res += 1
        return res 
    

    def dump(self):
        if self.head == None:
            return 
        dump = str(self.head.val)
        current = self.head.next
        while current:
            dump += "->" + str(current.val)
            current = current.next
        print(dump)
    

    def add_front(self,x):
        if self.head == None:
            self.head = Node(x)
        else:
            front = Node(x)
            front.next = self.head 
            self.head = front
    

    def add_back(self,x):
       if self.head == None:
            self.head = Node(x) 
       else:
            back = Node(x)
            current = self.head
            while current.next:
                current = current.next
            current.next = back


    def pop_front(self):
        if self.head == None:
            return
        self.head = self.head.next


    def pop_back(self):
        if self.head == None: 
            return 
        if self.head.next == None:
            self.head = None
            return
        current = self.head 
        while current.next.next:
            current = current.next 
        current.next = None


    def load_array(self,array):
        for e in array:
            self.push_back(e)


    def into_array(self):
        array = []
        current = self.head 
        while current != None:
            array.append(current.val)
            current = current.next
        return array


if __name__ == "__main__":
    l1 = LinkedList()
    l1.add_front(1)
    l1.add_front(2)
    l1.add_front(3)
    l1.add_front(4)
    l1.add_front(5)
    l1.dump()
    l1.pop_front()
    l1.dump()
    l1.pop_back()
    l1.dump()