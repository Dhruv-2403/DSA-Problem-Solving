class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        x=numBottles
        while numBottles>=numExchange:
            numBottles=numBottles-(numExchange-1)
            x+=1
            numExchange+=1
        return x
        