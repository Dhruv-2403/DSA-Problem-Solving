class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l=""
        for i in range(k-1,-1,-1):
            l+=s[i]

        for i in range(k,len(s)):
            l+=s[i]
        return l

        