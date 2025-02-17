class Solution:
    def minSubArrayLen(self, k: int, arr: List[int]) -> int:
       
        n = len(arr)
        min_length = float('inf')
        start = 0
        curr_sum = 0
        
        for end in range(n):
            curr_sum += arr[end]
            
            while curr_sum >= k:
                min_length = min(min_length, end - start + 1)
                curr_sum -= arr[start]
                start += 1
        
        return min_length if min_length != float('inf') else 0