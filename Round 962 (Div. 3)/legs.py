totalTests = int(input())
for _ in range(totalTests):
    legs = int(input())
    total = legs//4
    total += ((legs%4)//2)
    print(total)