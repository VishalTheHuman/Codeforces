totalTests = int(input())
results = []
for _ in range(totalTests):
    length = int(input())
    arr = list(map(int, input().split()))

    oddSum = evenSum = 0
    for idx, x in enumerate(arr):
        if idx%2==0: # 0 as odd idx
            oddSum += x
        else:
            evenSum += x
    oddCount = len(arr)//2 + len(arr)%2
    evenCount = len(arr)//2
    if (oddSum % oddCount) != 0 or (evenSum%evenCount) != 0 or ((oddSum/oddCount) != (evenSum/evenCount)):
        results.append("NO")
    else:
        results.append("YES")
        
print("\n".join(list(map(str,results))))