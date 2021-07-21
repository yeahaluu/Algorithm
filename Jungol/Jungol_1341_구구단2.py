def multiplication(s, e):
    # 범위(2~9)를 벗어나면 "input error!"를 출력하고 다시 입력 받는다.
    if s>9 or s<2 or e>9 or e<2:
        print("INPUT ERROR!")
        s, e = map(int, input().split())
        multiplication(s, e)
    else:
        # 입력된 구간의 범위는 증가하거나 감소하는 순서 그대로 출력되어야한다.
        # 따라서 더해지는 값 add +1 or -1로 한다.
        if s > e:
            add = -1
        else:
            add = 1

        # 5 * 1 =  5   4 * 1 =  4   3 * 1 =  3   다음과 같이 출력해야한다.
        for i in range(s, e + add, add):
            for j in range(1, 10):
                result = i*j
                if j%3 == 0:
                    if 0 <= result <= 9:
                        print('{} * {} =  {}'.format(i, j, result), end="   ")
                        print()
                    else:
                        print('{} * {} = {}'.format(i, j, result), end="   ")
                        print()
                else:
                    if 0 <= result <= 9:
                        print('{} * {} =  {}'.format(i, j, result), end="   ")
                    else:
                        print('{} * {} = {}'.format(i, j, result), end="   ")
            print()


s, e = map(int, input().split())

multiplication(s, e)