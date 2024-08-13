totalTests = int(input())
for _ in range(totalTests):
    num = input()
    if num[0] == "1":
        if len(num)==3: 
            if num[1]=="0" and num[2]>"1":
                print("YES")
            else:
                print("NO")
        elif len(num)>2 and num[1]=="0" and num[2]>="1":
            print("YES")
        else:
            print("NO")
    else:
        print("NO")