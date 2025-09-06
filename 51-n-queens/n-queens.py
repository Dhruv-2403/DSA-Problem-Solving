class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res=[]

        column=set()
        diag1=set()
        res=[]

        diag2=set()

        board=[["."]*n for _ in range(n)]
        
        def helper(row):
            if row==n:
                res.append(["".join(i) for i in board])
                return
            for i in range(n):
                if i in column or (row-i) in diag1 or row+i in diag2:
                    continue

                board[row][i]="Q"
                column.add(i)
                diag1.add(row-i)
                diag2.add(row+i)

                helper(row+1)

                board[row][i]="."
                column.remove(i)
                diag1.remove(row-i)
                diag2.remove(row+i)
        helper(0)
        return res

        