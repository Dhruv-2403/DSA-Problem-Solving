class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk=[]
        set1=set()
        d={}
        for i in range(len(s)):
            d[s[i]]=i
        # return d












        for i in range(len(s)):

            if s[i] not in set1:
                while stk and stk[-1]>s[i] and d[stk[-1]]>i:
                    set1.remove(stk.pop())
                stk.append(s[i])




                set1.add(s[i])
        return "".join(stk)




        
        