class Solution:
    def shipWithinDays(self, weights: List[int], d: int) ->int:
        
        left=max(weights)
        right=sum(weights)
        if d==1:
            return right
        if d>=len(weights):
            return left
        
        while left<=right:
            mid=(left+right)//2
            x=0
            count=1
            for i in weights:
                x+=i
                if x>mid:
                    count+=1
                    x=i
            if count<=d:
                right=mid-1
            else:
                left=mid+1
        return left