from collections import deque

if __name__ == "__main__":
    s = deque(input().rstrip())
    t = deque(input().rstrip())

    check = False
    while t:
        if t[-1] == 'A':
            t.pop()
        elif t[-1] == 'B':
            t.pop()
            t.reverse()

        if t == s:
            check = True
            break
    if check:
        print(1)
    else:
        print(0)