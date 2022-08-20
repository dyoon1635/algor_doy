n, k = map(int, input().split())
"""for i in range(int((n + 1) / 2) + 1):
    if (i + 1) * (n - i + 1) == k:
        print('YES')
        exit(0)
print('NO')"""

# a + b = n + 2
# a * b = k
# b = n + 2 -a
# therefore : a^2 - (n + 2)a + k = 0
tmp = (n + 2) **2 - 4 * k
a, b = ((n + 2) - tmp ** 0.5) / 2, ((n + 2) + tmp ** 0.5) / 2
if tmp < 0 or int(tmp ** 0.5) ** 2 != tmp or \
        int(a) != a or int(b) != b or a <= 0 or b <= 0:
    print('NO')
    exit(0)
print('YES')
