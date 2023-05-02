import sys
input = sys.stdin.readline

for _ in range(int(input())):
    command = list(input().strip())
    n = int(input())
    arr = list(input().strip()[1:-1].split(','))

    lp, rp, dir = 0, n, 1
    for each_command in command:
        if each_command == 'R':
            dir *= -1
        else: # D
            if dir == 1:
                lp += 1
            else: # dir == -1
                rp -= 1
        if lp > rp:
            break
    else:
        if dir == 1:
            print('[' + ','.join(arr[lp:rp]) + ']')
        else:
            print('[' + ','.join(reversed(arr[lp:rp])) + ']')
        continue
    print('error')
