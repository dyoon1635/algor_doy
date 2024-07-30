import sys, math
input = sys.stdin.readline

def EEA(a, b):
    k = a
    s0, s1, t0, t1 = 1, 0, 0, 1
    while b:
        q, r = divmod(a, b)
        a, b = b, r
        s, t = s0 - q * s1, t0 - q * t1
        s0, s1 = s1, s
        t0, t1 = t1, t
    if a != 1 or t0 > 10 ** 9:
        return 'IMPOSSIBLE'
    return (t0 % k + k) % k

for _ in range(int(input())):
    k, c = map(int, input().split())
    if math.gcd(k, c) != 1:
        print('IMPOSSIBLE')
        continue

    if c == 1:
        print('IMPOSSIBLE' if k + 1 > 10 ** 9 else k + 1)
        continue
    if k == 1:
        print(1)
        continue
    print(EEA(k, c))

