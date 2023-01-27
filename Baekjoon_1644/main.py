from math import *
n = int(input())
if n < 3:
    print(n - 1)
    exit(0)

prime = []
for i in range(2, n + 1):
    check = True
    for j in range(2, int(ceil(sqrt(i))) + 1):
        if i != j and i % j == 0:
            check = False
            break
    if check: prime.append(i)

start, end = 0, 0
answer, total = 0, 2
while True:
    if total == n: answer += 1

    if total > n:
        total -= prime[start]
        if start > end: break
        start += 1
    elif total <= n:
        end += 1
        if end >= len(prime): break
        total += prime[end]
print(answer)