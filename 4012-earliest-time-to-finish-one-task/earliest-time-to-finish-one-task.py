class Solution(object):
    def earliestTime(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """

        l=[]
        for i in tasks:
            x=sum(i)
            l.append(x)
        return min(l)
        