class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # return edges








        d={}

        for i in edges:
            for j in i:




                if j in d:
                    d[j]+=1
                else:
                    d[j]=1
        # return d
        for i,j in d.items():
            if j==len(edges):
                return i












        
        

        