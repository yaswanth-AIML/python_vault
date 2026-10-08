class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        li=[]
        rows=len(matrix)
        column=len(matrix[0])
        for i in range(rows):
            for j in range(column):
                if matrix[i][j]==0:
                    li.append((i,j))
        for (i,j) in li:
            for col in range(column):
                matrix[i][col]=0
            for row in range(rows):
                matrix[row][j]=0
