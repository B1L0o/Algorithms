from node import DNode

class LinkedList:

    def __init__(self):
        self.head = None 
        self.tail = None 
        self.length = 0


    def push_front(self,x):
        node = DNode(x)

        if self.length == 0:
            self.head = node
            self.tail = node

        else:
            head = self.head 
            head.prev = node 
            node.next = head 
            self.head = node

        self.length += 1


    def pop_front(self):
        if self.length == 0:
            return
        
        res = self.head.val
        if self.length == 1:
            self.head = None 
            self.tail = None
        
        else:
            self.head = self.head.next
            self.head.prev = None

        self.length -= 1
        return res

    
    def push_back(self,x):
        node = DNode(x)
        tail = self.tail

        if self.length == 0:
            self.tail = node
            self.head = node

        else: 
            tail.next = node 
            node.prev = tail 
            self.tail = node
        
        self.length += 1


    def pop_back(self):
        if self.length == 0:
            return
        
        res = self.tail.val
        if self.length == 1:
            self.head = None 
            self.tail = None
        
        else:
            self.tail = self.tail.prev 
            self.tail.next = None

        self.length -= 1
        return res


    def find(self,x):
        if self.length == 0:
            return -1

        current = self.head
        pos = 0
        while current != None:
            if current.val == x:
                return pos 
            current = current.next
            pos += 1
        return -1
    

    def get(self,pos):
        if pos < 0 or pos > self.length:
            return 
        
        current = self.head 
        for _ in range(pos):
            current = current.next 
        return current.val


    def delete(self,x):
        if self.find(x) == -1:
            return

        if self.head.val == x:
            self.pop_front()
            return

        current=self.head 
        while current.val != x:
            current = current.next

        if current != self.tail:
            current.prev.next = current.next 
            current.next.prev = current.prev
        
        else:
            self.tail = current.prev 
            self.tail.next = None

        self.length -= 1

    
    def delete_all(self,x):
        while self.find(x) != -1:
            self.delete(x)


    def insert(self,pos,x):
        if pos < 0 or pos > self.length:
            return 
        
        if pos == 0:
            self.push_front(x)

        elif pos == self.length:
            self.push_back(x)

        else:
            node = DNode(x)
            current = self.head 
            for _ in range(pos-1):
                current = current.next
            current.next.prev = node 
            current.next = node
            self.length += 1


    def remove(self,pos):
        if pos < 0 or pos > self.length-1:
            return 
        
        # Useless conditionals but helps for clarity
        if pos == 0:
            return self.pop_front()

        elif pos == self.length-1:
            return self.pop_back()

        else:
            current = self.head 
            for _ in range(pos-1):
                current = current.next
            
            res = current.next.val
            current.next.next.prev = current 
            current.next = current.next.next
            self.length -= 1
            return res


    def destroy(self):
        while self.length > 0:
            self.pop_front()


    def dump(self):
        print(f"\nThe list has {self.length} nodes.\n")
        if self.length == 0:
            return 

        output = "head --> " + str(self.head.val)
        current = self.head.next
        while current != None:
            output += " --> " + str(current.val)
            current = current.next
        output += " <-- tail"
        print(output)


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


    def reverse(self):
        for pos in range(self.length-1,-1,-1):
            x = self.get(pos)
            self.push_back(x)
            self.remove(pos)

if __name__ == "__main__":
    l = LinkedList()

    text = "\n\nList of instructions: \n\n"
    text += "push_front\tPushes an element at the beginning of the list.\n"
    text += "push_back\tPushes an element at the end of the list.\n"
    text += "pop_front\tRemoves the first element of the list.\n"
    text += "pop_back\tRemoves the last element of the list.\n"
    text += "dump\t\tPrints the list.\n"
    text += "reverse\t\tReverse the list.\n"
    text += "get\t\tReturns the value at the given index.\n" 
    text += "insert\t\tInserts value at given index.\n"
    text += "remove\t\tRemoves node at given index\n"
    text += "destroy\t\tRemoves all nodes\n"
    text += "delete\t\tRemoves first node with given value\n"
    text += "delete_all\tRemoves all nodes with give value\n"
    text += "find\t\tReturns first position of value in the list\n"
    text += "load_array\tLoads the list from an array"

    print("Type 'help' for help")

    while True:
        key = input("\n---What do you want to do ?---\n\n> ")
        match key:

            case "push_front":
                x = int(input("\nEnter a number to insert at the beginning:\n\n> "))
                l.push_front(x)
                l.dump()

            case "push_back":
                x = int(input("\nEnter a number to insert at the end:\n\n> "))
                l.push_back(x)
                l.dump()

            case "pop_front":
                l.pop_front()
                l.dump()

            case "pop_back":
                l.pop_front()
                l.dump()

            case "dump":
                l.dump()

            case "reverse":
                l.reverse()
                l.dump()

            case "get":
                x = int(input("\nEnter node position:\n\n> "))
                print(f"\n\nThe {x}th node has value {l.get()}")
                l.dump()

            case "insert":
                x = int(input("\nEnter a number to insert:\n\n> "))
                pos = int(input("\nWhere to insert it ?\n\n> "))
                l.insert(x,pos)
                l.dump()

            case "remove":
                pos = int(input("\nEnter the position of the node to delete ?\n\n> "))
                l.remove(pos)
                l.dump()

            case "destroy":
                l.destroy()
                print("\n\nThe list has been destroyed.")

            case "delete":
                x = int(input("\nEnter the value to delete: \n\n> "))
                l.delete(x)
                l.dump()

            case "delete_all":
                x = int(input("\nEnter the value to delete: \n\n> "))
                l.delete_all(x)
                l.dump()

            case "find":
                x = int(input("\nEnter the node value of the node: \n\n> "))
                print(f"\n\nThe first node with value {x} is at position  {l.find(x)}")

            case "load_array":
                arg = input("\nEnter sequence of numbers: \t\t\tEx: 1 2 3 4 5 ...\n\n> ").split()
                array = [int(x) for x in arg]
                l.load_array(array)
                l.dump()

            case "help":
                print(text)

            case "quit":
                exit()

            case _: 
                print("\n\nNot a valid command. Type 'quit' to quit\n")