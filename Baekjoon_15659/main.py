import sys
input = sys.stdin.readline

def backtracking(idx, op, exp):
    global max_val, min_val
    if idx >= len(nums):
        result = eval(exp)
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return

    add, minus, mul, div = op
    if add: backtracking(idx + 1, [add - 1, minus, mul, div], exp + "+" + str(nums[idx]))
    if minus: backtracking(idx + 1, [add, minus - 1, mul, div], exp + "-" + str(nums[idx]))
    if mul: backtracking(idx + 1, [add, minus, mul - 1, div], exp + "*" + str(nums[idx]))
    if div: backtracking(idx + 1, [add, minus, mul, div - 1], exp + "//" + str(nums[idx]))

n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split())) # + - * /

max_val, min_val = -sys.maxsize, sys.maxsize
backtracking(1, ops, str(nums[0]))
print('{}\n{}'.format(max_val, min_val))