class Solution(object):
    def minimizeSum(self, a):
        """
        :type nums: List[int]
        :rtype: int
        """
        a.sort()
        return min(a[-1]-a[2],a[-2]-a[1],a[-3]-a[0])
        