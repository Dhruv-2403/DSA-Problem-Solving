class Solution(object):
    def countEven(self, num):
        count=0
        for i in range(2,num+1):
            s=str(i)
            l=[]
            for i in s:
                l.append(int(i))
            if sum(l)%2==0:
                count+=1
        return count

        