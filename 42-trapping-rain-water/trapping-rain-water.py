class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left=0
        right=len(height)-1

        l=height[left]
        r=height[right]




        trap=0
        while left<right:
            if l<r:
                left+=1
                l=max(l,height[left])
                trap+=l-height[left]
            else:
                right-=1
                r=max(r,height[right])
                trap+=r-height[right]
        return trap


        