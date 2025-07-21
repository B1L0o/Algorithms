class segmentTree:
    def __init__(n,self):
        #size of the tree can not be more than 4times the array's size
        self.pos= [0] * 4*n

    # build has to be called with n-1 as right value
    def build(self,arr,right,left=0,segment=1):
        if (left == right):
            self.pos[segment] = arr[left]
            return
        mid = (right+left)//2
        self.build(arr,mid,left,segment*2)
        self.build(arr,right,mid,segment*2 + 1)
        self.pos[segment] = self.pos[segment*2] + self.pos[segment*2+1]

    def update(self,segment,left,right,position,new_value)

