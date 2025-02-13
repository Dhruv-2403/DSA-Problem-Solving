class Solution:
    def finalString(self, s: str) -> str:
        l=[]
        for i in s:
            if i!="i":
                l.append(i)
            if i=="i":
                l=l[::-1]
        return "".join(map(str,l))

        