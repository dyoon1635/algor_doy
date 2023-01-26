n = int(input())
score = list(map(int, input().split()))
score.sort()
total = sum(score)
if len(score) != n or total != (n * (n - 1)) // 2:
    print(-1)
    exit(0)

s1, s2 = 0, 0
for i, each in enumerate(score):
    s1 += i
    s2 += each
    if s1 > s2:
        print(-1)
        exit(0)
print(1)