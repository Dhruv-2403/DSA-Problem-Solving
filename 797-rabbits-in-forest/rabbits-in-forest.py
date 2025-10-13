import math
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        d={}
        for i in answers:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        x=0
        for i in d:
            x+=(ceil(float(d[i])/(i+1))*(i+1))
        return int(x)
