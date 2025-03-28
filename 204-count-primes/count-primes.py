class Solution:
    def countPrimes(self, n: int) -> int:

       
        prime=[True]*(n+1)
        p=2
        while p*p<=n:
            if prime[p]==True:
                for i in range(p*p,n+1,p):
                    prime[i]=False
            p+=1

        l=[]
        for i in range(2,n):
            if prime[i]:
                l.append(i)
        count=0
        for i in l:
            count+=1
        return count
        