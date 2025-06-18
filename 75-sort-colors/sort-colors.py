class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # low, high, mid = 0, len(nums) - 1, 0

        # while mid <= high:
        #     if nums[mid] == 0:
        #         nums[low], nums[mid] = nums[mid], nums[low]
        #         low += 1
        #         mid += 1
        #     elif nums[mid] == 1:
        #         mid += 1
        #     else:
        #         nums[mid], nums[high] = nums[high], nums[mid]
        #         high -= 1



        for i in range(len(nums)):
            x=nums[i]

            j=i-1

            while j>=0 and x<nums[j]:
                nums[j+1]=nums[j]

                j-=1

            nums[j+1]=x

        return nums

