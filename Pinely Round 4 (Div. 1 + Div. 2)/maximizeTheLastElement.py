totalTests = int(input())
for _ in range(totalTests):
    N = int(input())
    arr = list(map(int, input().split(" ")))
    while len(arr) > 1: 
        idx = -1
        minVal = float("inf")
        for i in range(1, len(arr)):
            val = arr[i] + arr[i-1]
            if val < minVal:
                minVal = val
                idx = i
        arr = arr[:idx-1] + arr[idx+1:]
    print(arr[0])