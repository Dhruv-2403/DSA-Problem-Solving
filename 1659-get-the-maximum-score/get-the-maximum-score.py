class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i=0
        j=0
        x=0
        y=0
        ans=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                x+=nums1[i]
                i+=1
            elif nums2[j]<nums1[i]:
                y+=nums2[j]
                j+=1
            else:
                ans+=max(x,y)+nums1[i]
                i+=1
                j+=1
                x=0
                y=0

        while i<len(nums1):
            x+=nums1[i]
            i+=1
        while j<len(nums2):
            y+=nums2[j]
            j+=1
        return (ans+max(x,y))%(10**9+7)


