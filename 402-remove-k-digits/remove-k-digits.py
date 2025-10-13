class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stk=[]
        stk.append(num[0])
        for i in range(1,len(num)):

            dig=num[i]
            while stk and stk[-1]>dig and k>0:
                stk.pop()
                k-=1
            stk.append(dig)
        while k:
            stk.pop()
            k-=1


        res="".join(stk).lstrip("0")
        if res!="":
            return res
        else:
            return "0"

        

