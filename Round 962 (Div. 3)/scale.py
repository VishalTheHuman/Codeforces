totalTests = int(input())
for _ in range(totalTests):
    n,k = list(map(int, input().strip().split(" ")))
    matrix = []
    for __ in range(n):
        matrix.append(list(input()))
    
    result = [[0]*(n//k) for temp in range(n//k)]
    current = [0, 0]
    for i in range(0, len(matrix), k):
        for j in range(0, len(matrix), k):
            result[current[0]][current[1]] = matrix[i][j]
            current[1] += 1
        current[0] += 1
        current[1] = 0
    for i in range(len(result)):
        print("".join(result[i]))