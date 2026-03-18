class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        fin_alpha = []
        for word in words:
            temp = 0
            for char in word:
                temp += weights[ord(char) - ord('a')]
    
            fin_alpha.append(chr(ord('z') - (temp%26)))
        return ''.join(fin_alpha)