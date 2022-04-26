N, K = map(int, input().split())
member = [i+1 for i in range(N)]
s = 1
answer = []

while len(member) > 0:
    s_index = member.index(s)
    e_index = (s_index+K-1) % len(member)
    answer.append(member[e_index])
    member.pop(e_index)
    if member:
        e_index = e_index % len(member)
        s = member[e_index]

print("<", end='')
for j in range(N-1):
    print(answer[j], end=', ')
print('{}>'.format(answer[N-1]))