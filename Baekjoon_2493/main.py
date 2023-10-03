n = int(input())
tower = [100000000] + list(map(int, input().split()))
res = [0 for _ in range(n + 1)]
stack = [(1, tower[1])]

for cur_idx in range(2, n + 1):
    cur_h = tower[cur_idx]
    while stack:
        top_idx, top_h = stack[-1]
        if top_h < cur_h: stack.pop()
        else: break

    if not stack: res[cur_idx] = 0
    else: res[cur_idx] = stack[-1][0]
    stack.append((cur_idx, cur_h))
print(*res[1:])