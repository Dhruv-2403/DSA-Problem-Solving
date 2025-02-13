class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l=0
        r=n-1

        top=0
        bottom=n-1
        l2=[[0]*n for _ in range(n)]
        x=1
        while l<=r and top<=bottom:

            for j in range(l,r+1):
                l2[top][j]=x
                x+=1
            top+=1

            for i in range(top,bottom+1):
                l2[i][r]=x
                x+=1
            r-=1
            if top<=bottom:
                for j in range(r,l-1,-1):
                    l2[bottom][j]=x
                    x+=1

                bottom-=1
            if l<=r:
                for i in range(bottom,top-1,-1):
                    l2[i][l]=x
                    x+=1
                l+=1
        return l2