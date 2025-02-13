class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        total_score=0
        
        l=0
        r=len(tokens)-1
        max1=0
        while l<=r:
            if power>=tokens[l]:
                power-=tokens[l]
                total_score+=1
                max1=max(total_score,max1)
                l+=1

                
            elif total_score>0:
                power+=tokens[r]
                
                total_score-=1
                r-=1
                
            else:
                break
        return max1





        