class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """

        x=text.split(" ")

        




        count=0
        for i in x:
            for j in brokenLetters:
                if j in i:
                    break
            else:
                count+=1
                


            


            
        return count
        