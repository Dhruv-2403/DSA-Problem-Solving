class Solution(object):
    def longestConsecutive(self, nums):

        #O(n) due to hashmap function 
        s=set(nums) #O(1)
        count=0
        for i in s:
            if i-1 not in s:
                next_i=i+1
                l=1
                while next_i in s: #every element doesnt needs to be checked , only the starting point should be checked
                    l+=1
                    next_i+=1
                
                count=max(count,l)
        return count


        