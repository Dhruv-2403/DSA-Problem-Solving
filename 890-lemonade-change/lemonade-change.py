class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """



        fiv=0

        te=0
        for i in bills:

        





            if i==5:
                fiv+=1
            elif i==10:
                if fiv==0:
                    return False
                fiv-=1
                te+=1
            else:
                if te>0 and fiv>0:
                    te-=1
                    fiv-=1
                elif fiv>=3:
                    fiv-=3
                else:
                    return False
        return True
            
        
        