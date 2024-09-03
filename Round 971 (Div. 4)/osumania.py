totalTests = int(input())
for _ in range(totalTests): 
    N = int(input())
    arr = [input() for __ in range(N)][::-1]
    result = []
    for x in arr: 
        result.append(x.index("#")+1)
    print(" ".join(list(map(str, result))))