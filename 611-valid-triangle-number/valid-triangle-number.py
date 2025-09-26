class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort() 
        l2=[]
        for i in range(len(nums)-1,-1,-1):




            l=0
            r=i-1
            count=0
            while l<r:
                if nums[l]+nums[r]>nums[i]:
                    count+=r-l
                    r-=1
                else:
                    l+=1
            

            l2.append(count)
        return sum(l2)









        
        