N = 4
def transpose(A,B):
    for i in range(N):
        for j in range(N):
            B[i][j] = A[j][i]

A = [[1,2,3],[4,5,6],[7,8,9]]

B = A[:][:]

transpose(A,B)
print("Result matrix is")
for i in range(N):
    for j in range(N):
        print(B[i][j], end = " ")
        print()