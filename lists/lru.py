class Node:

    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None 
        self.prev=None


class LRU:

    def __init__(self,capacity):
        self.size=0
        self.capacity = capacity
        self.head=None 
        self.tail=None 
        self.map = {}


    def insert(self,key,value):
        node = Node(key,value)

        if self.size==0:
            self.head=node 
            self.tail=node 
        
        else:
            head = self.head 
            self.head=node 
            node.next=head 
            head.prev=node

        return node


    def remove(node):
        node.next.prev = node.prev 
        node.prev.next = node.next


    def get(self,key):
        if key not in self.map:
            return -1 
        
        res = self.map[key][0]
        node = self.map[key][1]
        self.remove(node)
        self.map[key][1] = self.insert(key,res)
        return res


    def put(self,key,value):
        #TODO