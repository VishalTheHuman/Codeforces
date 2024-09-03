totalTests = int(input())
for _ in range(totalTests): 
    a, b = list(map(int, input().split()))
    minimum = float("inf")
    for c in range(a, b+1): 
        minimum = min(minimum, (c-a + b-c))
    print(minimum)