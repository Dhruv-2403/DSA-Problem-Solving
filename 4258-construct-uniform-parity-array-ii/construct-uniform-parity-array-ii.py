class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        counto=0
        counte=0
        odd=False
        mini=float("inf")
        for i in range(len(nums1)):
            if nums1[i]%2==1:
                
                odd=True
                mini=min(mini,nums1[i])
        
        # return euk 
        if not odd:
            return True
        for i in nums1:
            if i%2==0 and mini>i:
                return False

        return True