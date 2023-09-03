def solve(t):
    if len(t) == 0: return
    if t == S:
        print(1)
        exit(0)
    if t[-1] == 'A': solve(t[:-1])
    if t[0] == 'B': solve(list(reversed(t[1:])))

S = list(input())
T = list(input())
MaxLen = len(T)
solve(T)
print(0)