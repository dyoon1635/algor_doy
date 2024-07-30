n, a = map(int, input().split())

def EEA(a, b):
    r1, r2 = a, b
    s1, s2, t1, t2 = 1, 0, 0, 1
    while r2:
        q, r = divmod(r1, r2)
        s, t = s1 - q * s2, t1 - q * t2

        r1, r2 = r2, r
        s1, s2 = s2, s
        t1, t2 = t2, t
    return (t1 % a + a) % a if r1 == 1 else -1

print(n - a, EEA(n, a))