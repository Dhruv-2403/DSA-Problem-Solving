class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l=[]
        
        
        small=[]
        large=[]
        for i in nums:
            if i<pivot:
                small.append(i)
            if i>pivot:
                large.append(i)
            if i==pivot:
                l.append(pivot)
        
        return small+l+large
        