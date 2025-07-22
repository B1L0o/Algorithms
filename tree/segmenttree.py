# Iterative way

# Segment tree for sum
class segmentTree_IS:
    def __init__(self,array):
        #size of the tree can not be more than 2times the array's size
        n=len(array)
        self.size = n
        self.tree = [0] * 2*n
        self.build(array)

    def build(self,array):
        # Copy first half
        for i in range(self.size):
            self.tree[self.size+i] = array[i]
        # Compute second half
        for i in range(self.size-1,0,-1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i + 1]

    def update(self,pos,value):
        pos+=self.size
        self.tree[pos]=value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2*pos] + self.tree[2*pos + 1]

    def range_sum(self,left,right):
        res=0
        left+=self.size 
        right+=self.size 
        while left < right: 
            if left%2==1:
                res += self.tree[left]
                left += 1
            if right%2==1: 
                right -= 1
                res += self.tree[right]
            right //=2 
            left //= 2
        return res

# Segment tree for maximum

class segmentTree_IM:
    def __init__(self,array):
        n=len(array)
        self.size = n
        self.tree = [0] * 2*n
        self.build(array)

    def build(self,array):
        for i in range(self.size):
            self.tree[self.size+i] = array[i]
        for i in range(self.size-1,0,-1):
            self.tree[i] = max(self.tree[2*i],self.tree[2*i + 1])

    def update(self,pos,value):
        pos+=self.size
        self.tree[pos]=value
        while pos > 1:
            pos //= 2
            self.tree[pos] = max(self.tree[2*pos], self.tree[2*pos + 1])

    def range_max(self,left,right):
        res=0
        left+=self.size 
        right+=self.size 
        while left < right: 
            if left%2==1:
                res = max(res,self.tree[left])
                left += 1
            if right%2==1: 
                res = max(self.tree[right],res)
                right -= 1
            right //=2 
            left //= 2
        return res


# Recursive way

#TODO

if __name__ == "__main__":
    arr = [1, 2, 8, 4, 5]
    st = segmentTree_IM(arr)
    print(st.range_max(1, 4))  
    st.update(2, 10)           
    print(st.range_max(1, 4)) 

