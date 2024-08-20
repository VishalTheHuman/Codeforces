totalTests = int(input())
for _ in range(totalTests):
    N = int(input())
    points = list(map(int, input().split()))
    if N > 2:
        print("NO")
    elif abs(points[0]-points[1]) == 1:
        print("NO")
    else:
        print("YES")