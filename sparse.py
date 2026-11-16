a=[[1,0,0],
   [0,0,2],
   [0,0,0]]
rows=len(a)
cols=len(a[0])
zero=0
for i in range(rows):
    for j in range(cols):
        if a[i][j]==0:
            zero= zero+1
if zero > (rows * cols)/2:
    print("Matrix is Sparse")
else:
    print("Matrix is not Sparse")