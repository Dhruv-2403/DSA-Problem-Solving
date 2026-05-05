class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        l=[]
        s=str(n)
        for i in range(len(s)-1,-1,-1):
            l.append(int(s[i]))
        n2="".join(map(str,l))
        r=int(n2)
        count=0

        def is_prime(n):
            if n==1:
                return False

            if n==2 or n==3:
                return True
            for j in range(2,n):
                if n%j==0:
                    return False

            return True

        for i in range(min(n,r),max(n,r)+1):
            if is_prime(i):
                count+=i
        return count






        


        