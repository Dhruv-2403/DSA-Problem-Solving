class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

     
        # count=0
        # for i in range(len(nums)):
        #     if nums[i]==0:
        #         count+=1
        # if count>0:
        #     for i in range(len(nums)):
        #         if nums[i]==0:
        #             nums.append(0)
        #             nums.remove(nums[i])
                
        #         else:
        #             continue
        # else:
        #     return nums


        j=0
        for i in range(len(nums)):
            if nums[i]!=0:


                nums[j]=nums[i]
                j+=1
        while j<len(nums):
            nums[j]=0
            j+=1






                
                

        


        