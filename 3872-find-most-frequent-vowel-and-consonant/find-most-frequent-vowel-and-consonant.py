class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """

        vo={}
        co={}
        for i in s:
            if i in {"a","e","i","o","u"}:
                if i not in vo:
                    vo[i]=1
                else:
                    vo[i]+=1
            else:
                if i not in co:
                    co[i]=1
                else:
                    co[i]+=1
        
       
 
     
            
        if len(co)==0:

            return max(vo.values())
        if len(vo)==0:
            return max(co.values())
        else:
            return max(co.values())+max(vo.values())
        
        