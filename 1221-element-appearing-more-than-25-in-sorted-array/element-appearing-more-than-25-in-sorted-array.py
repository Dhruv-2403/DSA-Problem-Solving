class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1

    
        x=max(d.values())
        for i in d.keys():

            if d[i]==x and x>=len(arr)//x:
                return i
            
        else:
            return max(d.keys())
        