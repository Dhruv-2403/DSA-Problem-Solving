class Solution(object):
    
    def even_sum(self, n):
    
        return n * (n + 1)
    
    def odd_sum(self, n):
       
        return n * n
    
    def find_gcd(self, a, b):

        if b == 0:
            return a
        return self.find_gcd(b, a % b)
    
    def gcdOfOddEvenSums(self, n):
        even = self.even_sum(n)
        odd = self.odd_sum(n)
        return self.find_gcd(even, odd)