class Solution(object):
    def summaryRanges(self, nums):
        l=[]

        # count=0
        # for i in range(len(nums)-1):
        #     if nums[i]+1 in nums:
        #         count+=1
        #     else:
        #         count=0
        #         l.append(nums[i])
        # return count
        if nums==[]:
            return []
        x=nums[0]

        y=nums[0]

        for i in nums[1:]:
            if i==y+1:
                y=i
            else:
                if x==y:
                    l.append(str(x))
                else:
                    l.append(str(x)+"->"+str(y))
                x=i
                y=i
        if x==y:
            l.append(str(x))
        else:
            l.append(str(x)+"->"+str(y))
        return l

        







        
        