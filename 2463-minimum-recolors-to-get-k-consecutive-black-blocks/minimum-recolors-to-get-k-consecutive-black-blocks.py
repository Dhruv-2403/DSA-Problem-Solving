class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        x=float("inf")
        for i in range(len(blocks)-k+1):
            count=0
            for j in range(i,i+k):
                if blocks[j]=="W":
                    count+=1
            x=min(x,count)
        return x





            
        