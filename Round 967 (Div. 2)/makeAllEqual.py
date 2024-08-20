from collections import Counter
totalTests = int(input())
result = []
for _ in range(totalTests):
    N = int(input())
    arr = list(map(int, input().split()))
    result.append(N - max(Counter(arr).values()))
    
print("\n".join(list(map(str, result))))