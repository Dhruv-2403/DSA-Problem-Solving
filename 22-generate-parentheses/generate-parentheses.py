class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l=[]
        def helper(opp,cl,s):
            if opp==cl and opp+cl==2*n:
                l.append(s)
                return 
            if opp<n:
                helper(opp+1,cl,s+"(")
            if cl<opp:
                helper(opp,cl+1,s+")")
        helper(0,0,"")
        return l
                