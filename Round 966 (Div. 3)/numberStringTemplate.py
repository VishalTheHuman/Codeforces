totalTests = int(input())
storeVar = {}
storeNum = {}
for _ in range(totalTests):
    N = int(input())
    arr = list(map(int, input().split(" ")))
    stringCount = int(input())
    for _ in range(stringCount):
        possible = True
        string = input()
        if len(string) == N:
            for idx in range(N):
                if string[idx] not in storeVar and arr[idx] not in storeNum:
                    storeVar[string[idx]] = arr[idx]
                    storeNum[arr[idx]] = string[idx]
                elif string[idx] in storeVar and arr[idx] in storeNum:
                    if string[idx] != storeNum[arr[idx]] or arr[idx] != storeVar[string[idx]]:
                        possible = False
                        break 
                else:
                    possible = False
                    break
        else:
            possible = False
        
        if possible:
            print("YES")
        else:
            print("NO")
    
        storeNum.clear()
        storeVar.clear()