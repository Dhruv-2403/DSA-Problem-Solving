class Solution:
    def findKthLargest(self, l: List[int], k: int) -> int:
        l.sort(reverse=True)
        return l[k-1]