totalTests = int(input())

for _ in range(totalTests):
    l,r = list(map(int, input().split()))
    L,R = list(map(int, input().split()))
    doorsToLock = 0
    if not ((L-r) > 1 or (l-R) > 1):
        Right = (min(r,R)+ 1) if r!=R else R
        Left = max(l,L) - (0 if l==L else 1)
        for i in range(Left, Right):
            doorsToLock += 1
    print(doorsToLock if doorsToLock else 1)