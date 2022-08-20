N = int(input())
result = ''

def check():
    for i in range(1, int((len(result) + 1) / 2) + 1):
        if result[-i-i:-i] == result[-i:]:
            return False
    return True

def dfs():
    global result
    if N == len(result):
        print(result)
        exit(0)
    for next in ['1', '2', '3']:
        result = result + next
        if check(): dfs()
        result = result[:-1]
dfs()
