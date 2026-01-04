class Solution(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """

        for i in s[::-1]:
            if int(i)%2==0:
                break
            else:
                s=s[:len(s)-1]
        return s

        