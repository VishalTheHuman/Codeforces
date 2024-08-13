totalTests = int(input())
for _ in range(totalTests):
    N = int(input())
    arr = list(map(int, input().split(" ")))
    seats = [False]*N
    seats[arr[0]-1] = True
    isPossible = True
    for x in arr[1:]:
        x-=1
        if ((0<=(x-1) and seats[x-1]) or ((x+1)<N and seats[x+1])) and seats[x] == False:
            seats[x] = True
        else:
            isPossible = False
            break

    if isPossible:
        print("YES")
    else:
        print("NO")