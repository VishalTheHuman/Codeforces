totalTests = int(input())
results = []
for _ in range(totalTests):
    n, m = list(map(int, input().split()))
    words = []
    for __ in range(n):
        words.append(len(input()))
    totalWords = 0 
    currLength = 0
    idx = 0
    while currLength <= m and  idx < len(words):
        if currLength + words[idx] > m:
            break
        currLength += words[idx]
        totalWords += 1
        idx += 1
    results.append(totalWords)

print("\n".join(list(map(str,results))))