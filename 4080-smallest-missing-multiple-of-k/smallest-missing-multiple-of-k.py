class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:



        l=[]
        for i in range(len(nums)):
            if nums[i]%k==0:
                l.append(nums[i])
        for i in range(max(nums)):
            if i>0:
                if i%k==0 and i not in nums:
                    return i
        if l==[]:
            return k
        else:
            return max(l)+k
                
                
            
        