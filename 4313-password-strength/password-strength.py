class Solution:
    def passwordStrength(self, password: str) -> int:
        count=0
        ch=[False]*26
        up=[False]*26
        nu=[False]*26
        sp=[False]*26
        for i in password:
            if "a"<=i<="z":
                j=ord(i)-ord("a")
                if not ch[j]:
                    ch[j]=True


                    count+=1
            elif "A"<=i<="Z":
                j=ord(i)-ord("A")
                if not up[j]:
                    up[j]=True
                    count+=2
            elif "0"<=i<="9":
                j=ord(i)-ord("0")
                if not nu[j]:
                    nu[j]=True
                    count+=3
            else:
                j="!@#$".index(i)
                if not sp[j]:
                    sp[j]=True
                    count+=5
        return count
            



        