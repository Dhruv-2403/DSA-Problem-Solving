class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        hold=-prices[0]
        rest=0
        sold=0

        for i in prices[1:]:
            prev_hold=hold
            prev_rest=rest
            prev_sold=sold

            hold=max(prev_hold,prev_rest-i)
            sold=prev_hold+i
            rest=max(prev_rest,prev_sold)
        return max(sold,rest)




        