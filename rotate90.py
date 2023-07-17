def transpose(matrix,rows,cols):
    for i in range(rows):
        for j in range(i+1,cols):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    return matrix
def reverse_rows(matrix):
    reversed_matrix=[]
    for row in matrix:
        reversed_matrix.append(row[::-1])
    return reversed_matrix
matrix=[]
rows=int(input("Enter the no of rows:"))
cols=int(input("Enter the no of cols:"))
for i in range(rows):
    matrix.append(list(map(int,input("Enter elements:").split())))
transposed_matrix=transpose(matrix,rows,cols)
reversed_90=reverse_rows(transposed_matrix)
for row in reversed_90:
    print(row)
