totalTests = int(input().strip())
for _ in range(totalTests):
    n,m = tuple(map(int, input().strip().split(" ")))
    if n==1 and m==1:
        input()
        print(-1)
        continue
    matrix = [[0]*m for _ in range(n)]
    val = 1
    for i in range(n):
        matrix[i] = list(map(int,input().strip().split()))
    
    if n==1:
        print(" ".join(list(map(str,matrix[0][1:]+[matrix[0][0]]))))
        continue
    
    matrix = matrix[1:] + [matrix[0]]
    for x in matrix:
        x = list(map(str, x))
        print(" ".join(x))