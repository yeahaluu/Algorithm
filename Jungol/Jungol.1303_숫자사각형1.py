n, m = map(int, input().split())

result = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        result += 1
        print(result, end=" ")
    print()