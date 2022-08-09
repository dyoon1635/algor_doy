import sys
T = int(input())

def SUM(num):
    if num <= 0: return 0
    digit = [0] * 10

    num1, num2, d = 0, 0, 1
    while True:
        num1, num2 = num // (d * 10), num % (d * 10)
        if num1 == 0: break
        for i in range(10):
            digit[i] += num1 * d
        for i in range(1, (num2 // d)):
            digit[i] += d
        digit[num2 // d] += ((num % d) + 1)
        d *= 10
    for i in range(10):
        digit[i] += num1 * num2
    for i in range(1, (num2 // d)):
        digit[i] += d
    digit[num2 // d] += ((num % d) + 1)

    res = 0
    for idx, cnt in enumerate(digit):
        res += (idx * cnt)
    return res

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(SUM(b) - SUM(a - 1))

