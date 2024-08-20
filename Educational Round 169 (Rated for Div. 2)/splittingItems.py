totalTests = int(input())
for _ in range(totalTests):
    n, k = list(map(int, input().split()))
    costs = sorted(list(map(int, input().split())), reverse=True)
    A = costs[0]
    B = 0
    for i in range(1,len(costs)):
        if i%2==0:
            A += costs[i]
        else:
            if k>0:
                B += min(costs[i-1],costs[i]+k)
                k -= min(costs[i-1],costs[i]+k) - costs[i]
            else:
                B += costs[i]
    print(A-B)