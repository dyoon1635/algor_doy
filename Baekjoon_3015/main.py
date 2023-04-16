import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
stack, answer = [], 0

for each in arr:
    while stack and stack[-1][0] < each:
        answer += stack.pop()[1]

    if not stack:
        stack.append((each, 1))
        continue

    if stack[-1][0] == each:
        cnt = stack.pop()[1]
        answer += cnt
        if stack: answer += 1
        stack.append((each, cnt + 1))
    else:
        stack.append((each, 1))
        answer += 1
print(answer)