class Solution(object):
    def setZeroes(self, matrix):

        # zero_ro=[False]*len(matrix)
        # zero_co=[False]*(len(matrix[0]))
        x=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    x.append((i,j))
                    
                else:
                    continue
        # return x

        for i in range(len(x)):
            a,b=x[i]

            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if i==a or j==b:
                        matrix[i][j]=0
            
        
                
        
            


        
        