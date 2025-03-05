class Solution:
    def coloredCells(self, n: int) -> int:
        prefix=[1]
        for i in range(1,n+1):
            prefix.append(prefix[i-1]+4*i)
        return prefix[n-1]