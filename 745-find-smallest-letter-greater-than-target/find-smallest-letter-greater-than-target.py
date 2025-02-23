class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l=[]
        for i in letters:
            if ord(i)>ord(target):
                l.append(ord(i))
        if l==[]:
            return letters[0]
        else:
            return chr(l[0])

                
        