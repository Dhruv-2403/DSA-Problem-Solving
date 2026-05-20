class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        x=max(nums)
        d=[0]*(x+1)
        flag=[False]*(x+1)
        for i in nums:
            flag[i]=True
        for i in range(1,x+1):
            if not flag[i]:
                continue


            for j in range(i,x+1,i):
                if d[j]==0:
                    d[j]=i
        # return d
        sum1=0
        for i in nums:
            sum1+=(d[i])
        return sum1

            


        