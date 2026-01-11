class Solution(object):
    def centeredSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(len(nums)):
            sub=set()
            x=0
            for j in range(i,len(nums)):
                x+=nums[j]
                sub.add(nums[j])
                if x in sub:
                    count+=1
        return count
        


        

        