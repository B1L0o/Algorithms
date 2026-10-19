class Node:

    def __init__(self,val=0,left=None,right=None):
        self.right = right 
        self.left = left
        self.val = val


class BST:

    def __init__(self):
        self.root=None 


    def add(self,val):
        new = Node(val)
        if self.root == None:
            self.root = new 
            return 

        current = self.root
        while True:
            if val < current.val:
                if current.left == None:
                    current.left = new 
                    return 
                current = current.left 
            elif val > current.val:
                if current.right == None:
                    current.right = new 
                    return 
                current = current.right
            else:
                return
            
    def construct_from_array(self,arr):
        def constructTree(left,right):
            if left <= right:
                mid = (left + right) // 2 
                return Node(arr[mid], left = constructTree(left,mid-1), right=constructTree(mid+1,right))
            return None

        self.root = constructTree(0,len(arr)-1)

    def balance(self):
        arr=[]
        def sortBST(node):
            if node == None:
                return 
            sortBST(node.left)
            arr.append(node.val)
            sortBST(node.right)

        sortBST(self.root)
        self.construct_from_array(arr)
        
        

        