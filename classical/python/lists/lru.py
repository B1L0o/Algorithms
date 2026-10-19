# Least Recently Used (LRU) cache
class Node:
    def __init__(self,val = None,key=None):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = None 
        self.tail = None     
        self.map = {}   


    def insert(self, node):
        if self.size == 0:
            self.head = node
            self.tail = node

        else:
            head = self.head 
            head.prev = node
            node.next = head
            self.head = node

        self.size+=1

    def remove(self, node):
        if self.size == 1:
            self.head = None 
            self.tail = None

        elif self.head == node:
            self.head = self.head.next
            self.head.prev = None

        elif self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
            
        else:
            node.prev.next = node.next 
            node.next.prev = node.prev

        self.size -= 1


    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self.remove(node)
        self.insert(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])

        node = Node(value,key)
        self.insert(node)
        self.map[key] = node

        if self.size > self.capacity:
            self.map.pop(self.tail.key)
            self.remove(self.tail)