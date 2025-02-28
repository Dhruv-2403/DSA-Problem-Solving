class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations



    
    
        res = []  
            
            
        for r in range(len(nums) + 1):
            
                
            res.extend([list(comb) for comb in combinations(nums, r)])
  
        return res
                        
                        