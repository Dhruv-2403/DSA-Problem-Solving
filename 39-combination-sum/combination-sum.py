class Solution(object):
    def combinationSum(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        def helper(i,curr,total):
            if total==target:
                res.append(list(curr))


                return 
            if total>target:
                return 
            for j in range(i,len(nums)):
                curr.append(nums[j])
                helper(j,curr,total+nums[j])
                curr.pop()
        

        helper(0,[],0)
        return res