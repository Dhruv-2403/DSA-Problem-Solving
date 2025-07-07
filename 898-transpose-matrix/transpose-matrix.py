class Solution(object):
    def transpose(self, matrix):
        l=[]
        for i in range(len(matrix[0])):
            mat=[]
            for j in range(len(matrix)):
                mat.append(matrix[j][i])
            l.append(mat)
        return l
       