class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations

        x=permutations(nums)
        l=[]
        for i in list(x):
            l.append(i)
        return l
            
        