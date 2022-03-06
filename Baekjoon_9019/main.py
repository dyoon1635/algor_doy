from collections import deque

def D(num):
    return (2*num)%10000

def S(num):
    if num:
        return num-1
    return 9999

def L(num):
    return (num % 1000) * 10 + (num // 1000)

def R(num):
    return (num % 10) * 1000 + (num // 10)

def solve(a, b):
    tmp = deque()
    tmp.append([a, ''])
    check = set()
    check.add(a)
    cc = [0] * 10000
    while True:
        cur_num, step = tmp.popleft()
        cc[cur_num] += 1
        if cur_num == b:
            print(step)
            break
        next_num = D(cur_num)
        if next_num not in check:
            check.add(next_num)
            tmp.append([next_num, step + 'D'])

        next_num = S(cur_num)
        if next_num not in check:
            check.add(next_num)
            tmp.append([next_num, step + 'S'])

        next_num = L(cur_num)
        if next_num not in check:
            check.add(next_num)
            tmp.append([next_num, step + 'L'])

        next_num = R(cur_num)
        if next_num not in check:
            check.add(next_num)
            tmp.append([next_num, step + 'R'])

def main():
    for i in range(int(input())):
        A, B = map(int, input().split())
        solve(A, B)

if __name__ == "__main__":
    main()