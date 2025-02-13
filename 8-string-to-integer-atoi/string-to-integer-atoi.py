class Solution(object):
    def myAtoi(self, s):
        s=s.strip()
        if len(s)==0:
            return 0
        
        x=0
        z=1
        y=[]
        if s[0]=="-":
            z=-1
            x+=1
        if s[0]=="+":
            x+=1
        while x<len(s) and s[x].isdigit():
            y.append(s[x])
            x+=1
        if not y:
            return 0
        d= (int(("".join(y)))*z)

        if d<(-2**31):
            return (-2**31)
        elif d>(2**31-1):
            return (2**31-1)
        return d
        

        
        

      
            

        
        

                

        