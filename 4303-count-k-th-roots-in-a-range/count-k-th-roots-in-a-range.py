class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        count=0
        if k==1:
            return r-l+1
        for i in range(10**5+1):
            if l<=pow(i,k)<=r:
                count+=1
            if pow(i,k)>r:
                break
        return count
        
            
        