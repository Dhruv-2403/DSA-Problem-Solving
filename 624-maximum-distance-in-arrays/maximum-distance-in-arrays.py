class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """

        small=arrays[0][0]
        large=arrays[0][-1]
        max_d=0
        for i in range(1,len(arrays)):
            arr=arrays[i]
            max_d=max(max_d,abs(arr[-1]-small),abs(arr[0]-large))
            small=min(small,arr[0])
            large=max(large,arr[-1])
        return max_d







        