class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:
        ar=[a,b,c]
        ar.sort()
        if ar[0]+ar[1]<ar[2]:
            ar[2]=ar[1]+ar[0]
        
        return ar[2]-ar[0]        