class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        x=max(nums)
        z=1
        k=1
        for i in nums:
            y=z*i
            z=max(y,k*i,i)
            k=min(y,k*i,i)
            x=max(x,z)
        return x


        