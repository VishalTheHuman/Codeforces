import math

totalTests = int(input())
for _ in range(totalTests): 
    x,y,k = list(map(int, input().split()))
    xDir = math.ceil(x/k)
    yDir = math.ceil(y/k)
    if xDir > yDir:
        print(2*xDir-1)
    else:
        print(2*yDir)