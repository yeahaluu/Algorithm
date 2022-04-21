def permutations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutations(array[:i] + array[i+1:], r-1):
                yield [array[i]] + next

array = [1, 2, 3, 4]
r = 2
for i in permutations(array, r):
    print(i, end=" ")