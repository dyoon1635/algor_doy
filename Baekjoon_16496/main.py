from functools import cmp_to_key

n = int(input())

def compare(x, y):
    c1, c2 = x + y, y + x
    if c1 > c2: return -1
    return 1

arr = list(input().split())
check = True
for each in arr:
    if each != '0':
        check = False
        break
if check:
    print(0)
    exit(0)

arr.sort(key=cmp_to_key(compare))
for each in arr:
    print(each, end='')
