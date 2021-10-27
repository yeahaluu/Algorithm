for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = ((x2-x1)**2+(y2-y1)**2)**(1/2)
    # 더 큰거 r2
    if r2 < r1:
        r1, r2 = r2, r1
    # 조와 백이 같은 위치에 있을 때
    if r == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    # 조와 백이 같은 위치에 있지 않고 r > r2 일 때
    elif r2 < r:
        if r < r1 + r2:
            print(2)
        elif r == r1 + r2:
            print(1)
        else:
            print(0)
    # 조와 백이 같은 위치에 있지 않고 r < r2 일 때
    else:
        if r == r2 - r1:
            print(1)
        elif r > r2 - r1:
            print(2)
        else:
            print(0)