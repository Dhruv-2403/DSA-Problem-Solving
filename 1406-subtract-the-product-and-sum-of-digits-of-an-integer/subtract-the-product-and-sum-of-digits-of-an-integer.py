class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        prod=1
        sum1=0
        s=str(n)

        for i in s:
            prod*=int(i)
            sum1+=int(i)
        
        return prod-sum1
   

        