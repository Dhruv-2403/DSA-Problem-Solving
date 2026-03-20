from collections import defaultdict
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        d=defaultdict(int)
        n=len(arr)
        # d[0]=1
        # x=0
        o=0
        odd=0
        even=1
        res=0
        for i in range(len(arr)):
            o+=arr[i]
            if o%2==1:
                
                odd+=1
                res=res+even

            else:
                even+=1
                res=res+odd
        return res%(10**9+7)









        