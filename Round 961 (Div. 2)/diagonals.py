totalTests = int(input().strip())
for _ in range(totalTests):
    n, k = list(map(int, input().strip().split(" ")))
    if k==0:
        print(0)
        continue
    answer = 1
    k -= n
    curr = n-1
    while k>0:
        answer += 1
        if k<=curr:
            break
        k -= curr
        answer += 1
        k -= curr
        
        curr -=1
    print(answer)