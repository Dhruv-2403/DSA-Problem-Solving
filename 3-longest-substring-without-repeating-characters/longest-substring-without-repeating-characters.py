class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        stack=set()
        x=0
        y=0
        for i in range(len(s)):
            while s[i] in stack:
                stack.remove(s[x])
                x+=1
            stack.add(s[i])
            y=max(y,i-x+1)
        return y  

   
        