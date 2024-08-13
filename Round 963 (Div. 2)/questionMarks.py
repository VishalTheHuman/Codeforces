from collections import Counter
totalTests = int(input())
for _ in range(totalTests):
    n = int(input())
    answer = input()
    store = Counter(answer)
    result = 0
    for option, count in store.items():
        if option=="?":
            continue
        result += min(count, n)
    print(result)