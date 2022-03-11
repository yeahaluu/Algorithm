N = 1750
coin = [500, 100, 50, 10]

answer = 0

for c in coin:
  answer += N // c
  N %= c  # N = N & c

print(answer)