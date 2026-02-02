matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
matrix1=[]
for i in range(0,len(matrix)):
    row=[]
    for j in range(0,len(matrix)):
        l=len(matrix)-1
        row.append(matrix[l-j][i])
        l=l-1
    matrix1.append(row)
matrix[:]=matrix1
print(matrix)