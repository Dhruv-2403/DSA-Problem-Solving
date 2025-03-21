class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def solve(z):
            x=0
            for i in quantities:

                # for finding stores for each quantity
                x+=(i+z-1)//z 
            if x<=n:
                return True

           

            
   
        l=1         
        r=max(quantities)

        
        while l<r:
            mid=(l+r)//2

            if solve(mid):
            
                r=mid
            else:
                l=mid+1
        
        
        return l

        