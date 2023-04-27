import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    students = []
    books = [False for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        students.append((a, b))
    students.sort(key=lambda x: x[1])

    count = 0
    while students:
        a, b = students.pop(0)
        for idx in range(a, b + 1):
            if not books[idx]:
                books[idx] = True
                count += 1
                break
    print(count)