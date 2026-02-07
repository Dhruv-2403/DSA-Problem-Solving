class Solution(object):
    def countMonobit(self, n):
        """
        :type n: int
        :rtype: int
        """

        count=0
        for i in range(n+1):
            x=bin(i)[2:]
            if x.count("0")==len(x) or x.count("1")==len(x):
                count+=1
        return count
        