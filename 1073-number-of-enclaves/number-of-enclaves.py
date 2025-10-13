class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: in
        t
        
        """
        
        n=len(grid)
        m=len(grid[0])
        def dfs(i,j):
       
            if i==-1 or j==-1 or i==n or j==m or grid[i][j]==0:
                return 
            grid[i][j]=0
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)
        for i in range(n):
            for j in range(m):
                if (i==0 or j==0 or i==n-1 or j==m-1) and grid[i][j]==1:
                    dfs(i,j)
        x=0
        for i in range(n):
            for j in range(m):
                x+=grid[i][j]
        return x
