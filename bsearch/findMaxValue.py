# Leetcode 1552. Magnetic Force Between Two Balls - same as koko eats banana

# In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.
# Rick stated that magnetic force between two different balls at positions x and y is |x - y|.
# Given the integer array position and the integer m. Return the required force.

def maxDistance(position,m):
        def place_balls(gap):
            placed=[False] * len(position)
            placed[0] = True
            remaining=gap
            count=1
            for i in range(1,len(position)):
                remaining-=(position[i]-position[i-1])
                if remaining <= 0:
                    remaining = gap
                    placed[i] = True
                    count += 1
                if count == m:
                    break
            print(gap,placed)
            return count == m

        L = 1
        position.sort()
        R = position[-1]-position[0]

        while L < R:
            M = (L+R)//2 + 1
            if place_balls(M):
                L = M
            else:
                R = M - 1

        return L
