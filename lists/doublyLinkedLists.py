from node import DNode

class DoubleList:

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
        print(f"List has {self.length} nodes.")
        if self.length == 0:
            return 

        output = "head->" + str(self.head.val)
        current = self.head.next
        while current != None:
            output += " -> " + str(current.val)
            current = current.next
        output += "<-tail"
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
    l = DoubleList()

    text = "\n\nList of instructions: \n\n"
    text += "push_front - Pushes an element at the beginning of the list\n"
    text += "push_back - Pushes an element at the end of the list\n"
    text += "pop_front - Removes the first element of the list\n"
    text += "pop_back - Removes the last element of the list\n"
    text += "dump - Prints the list \n"
    text += "reverse - Reverse the lst \n"

    print("Type help for help")

    while True:
        key = input("\n\nWhat do you want to do ?\n")
        match key:
            case "push_front":
                x = int(input("Enter a number:\n"))
                l.push_front(x)
            case "push_back":
                x = int(input("Enter a number:\n"))
                l.push_back(x)
            case "pop_front":
                l.pop_front()
            case "pop_back":
                l.pop_front()
            case "dump":
                l.dump()
            case "help":
                print(text)
            case "quit":
                exit()