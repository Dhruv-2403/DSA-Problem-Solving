import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        # piles.sort()
        def helper(k):
            y=0
            for i in piles:
                y+=math.ceil(i/k)
            if y<=h:
                return True
            return False
        l=1
        h2=max(piles)
     
        while l<=h2: 
            mid=(l+h2)//2
            if helper(mid):
       
                h2=mid-1
            else:
                l=mid+1
        return l