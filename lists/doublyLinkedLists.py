from Node import DNode

class DoubleList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.length = 0

    def push_front(self,x):
        node = DNode(x)
        self.length += 1
        if self.head == None:
            self.head = node
            self.tail = node
            return 
        node.next = self.head 
        self.head = node
    
    #TODO