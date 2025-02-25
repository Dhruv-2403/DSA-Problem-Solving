class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        i=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                i=mid
                l=mid+1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
                
        l=0
        r=len(nums)-1
        j=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                j=mid
                r=mid-1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
               
                

        return j,i
        

                

        