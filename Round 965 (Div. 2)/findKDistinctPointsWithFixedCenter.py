totalTests = int(input())
for _ in range(totalTests):
    x_c, y_c, k = list(map(int, input().split(" ")))
    
    x = [-i+x_c for i in range(1, k//2 + 1)] + [i+x_c for i in range(1, k//2 + 1)] 
    y = [-i+y_c for i in range(1, k//2 + 1)] + [i+y_c for i in range(1, k//2 + 1)]
        
    if k % 2 == 1:
        x += [x_c]
        y += [y_c]
        
    for x_i, y_i in zip(x,y):
        print(f"{x_i} {y_i}")