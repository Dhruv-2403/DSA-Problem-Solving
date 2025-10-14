class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos=0
        neg=0
        max1=0
        for i in nums:
            if i==0:
                pos=0
                neg=0
            elif i>0:
                pos+=1
                if neg>0:
                    neg+=1
                else:
                    neg=0

            else:
                temp=pos

                
                
                if neg>0:
                    pos=neg+1
                else:
                    pos=0
                neg=temp+1
            max1=max(max1,pos)
        return max1
        
        