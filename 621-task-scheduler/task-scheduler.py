class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d={}
        for i in tasks:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1   
        max1=max(d.values())
        count=(n+1)*(max1-1)
        for i in d.values():
            if i==max1:
                count+=1
        return max(len(tasks),count)