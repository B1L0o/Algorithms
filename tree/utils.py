import math
from Algorithms.tree.bst import BST

def printTree(root):
        def height(node):
            if node == None:
                return -1
            return 1 + max(height(node.left),height(node.right))
        h=height(root)
        m=h+1
        n=int(math.pow(2,h+1)-1)
        mat=[["" for _ in range(n)] for _ in range(m)]

        def place_node(y,x,node,h):
            if node == None:
                return
            mat[y][x] = str(node.val)
            place_node(y+1,int(x-math.pow(2,h-y-1)),node.left,h)
            place_node(y+1,int(x+math.pow(2,h-y-1)),node.right,h)
        
        place_node(0,(n-1)//2,root,h)
        for line in mat:
            out = ""
            for char in line:
                if char == "":
                    out += " "
                else:
                    out += char 
            print(out)

if __name__ == "__main__":
    tree = BST()
    for i in range(100):
        tree.add(i)
    tree.balance()
    printTree(tree.root)
