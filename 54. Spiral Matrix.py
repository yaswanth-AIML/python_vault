class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        row=len(matrix)
        column=len(matrix[0])
        left=0
        right=column
        top=0
        bottom=row
        li=[]
        while left<right and top<bottom:
            for i in range(left,right):
                li.append(matrix[top][i])
            top+=1
            for i in range(top,bottom):
                li.append(matrix[i][right-1])
            right-=1
            if left>=right or top>=bottom:
                break
            for i in range(right-1,left-1,-1):
                li.append(matrix[bottom-1][i])
            bottom-=1
            for i in range(bottom-1,top-1,-1):
                li.append(matrix[i][left])
            left+=1
        return li
