class Solution(object):
    def maxWeight(self, pizzas):
        """
        :type pizzas: List[int]
        :rtype: int
        """
        n=len(pizzas)//4






        y,z=n//2,(n+1)//2
        pizzas.sort(reverse=True)
        return sum(pizzas[:z])+sum(pizzas[z+1:z+y+y+1:2])
        