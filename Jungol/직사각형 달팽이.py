dr = [0, 1, 0, -1]  # 우하좌상
dc = [1, 0, -1, 0]

n, m = map(int, input().split())

arr = [[0 for _ in range(m)] for _ in range(n)]
row = 0
col = -1
result = 1

for i in range(m):
    col += dc[0]
    arr[row][col] = result
    result += 1

# if m >= n:
#     round = (n-1)*2
# else:
#     round = ((m-1)*2) +1

for j in range(1, n):
    for k in range(1, 3):
        if j % 2 == 1 and k == 1:
            for _ in range(n-j):
                row += dr[1]
                arr[row][col] = result
                result += 1
        elif j % 2 == 1 and k == 2 :
            for _ in range(m-j):
                col += dc[2]
                arr[row][col] = result
                result += 1
        elif j % 2 == 0 and k == 1:
            for _ in range(n-j):
                row += dr[3]
                arr[row][col] = result
                result += 1
        else:
            for _ in range(m-j):
                col += dc[0]
                arr[row][col] = result
                result += 1

if m < n:
    if n % 2 == 1:
        for _ in range(n-m):
            row += dr[1]
            arr[row][col] = result
            result += 1
    else:
        for _ in range(n-m):
            row += dr[3]
            arr[row][col] = result
            result += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()


