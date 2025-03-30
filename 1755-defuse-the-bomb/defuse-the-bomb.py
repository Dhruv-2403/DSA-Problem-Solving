class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        e_code=code*2
        n=len(code)
     


        l=[]
        if k>0:
            
            for i in range(len(code)):
                l.append(sum(e_code[i+1:i+k+1]))
        else:
            k=abs(k)
            for i in range(len(code)):
                l.append(sum(e_code[i+n-k:i+n]))
        return l

           
    

           
