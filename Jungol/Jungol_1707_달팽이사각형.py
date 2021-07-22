dr = [0, 1, 0, -1]  # 우하좌상
dc = [1, 0, -1, 0]

n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]
row = 0
col = -1
result = 1

for _ in range(n):
    col += dc[0]
    arr[row][col] = result
    result += 1

for i in range(1, n):
    for j in range(1, 3):
        if i % 2 == 1 and j == 1:
            for _ in range(n-i):
                row += dr[1]
                arr[row][col] = result
                result += 1
        elif i % 2 == 1 and j == 2 :
            for _ in range(n-i):
                col += dc[2]
                arr[row][col] = result
                result += 1
        elif i % 2 == 0 and j == 1:
            for _ in range(n-i):
                row += dr[3]
                arr[row][col] = result
                result += 1
        else:
            for _ in range(n-i):
                col += dc[0]
                arr[row][col] = result
                result += 1


for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()


