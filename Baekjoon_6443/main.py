import sys, heapq
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def backtracking(string):
    if len(string) == length:
        result.add(string)
        return
    for idx in range(26):
        if alphabet[idx]:
            alphabet[idx] -= 1
            backtracking(string + chr(idx + 97))
            alphabet[idx] += 1


for _ in range(int(input())):
    word = sorted(list(input().strip()))
    length = len(word)
    alphabet = [0 for _ in range(26)]
    for each in word:
        alphabet[ord(each) - 97] += 1

    result = set()
    backtracking('')
    for each in sorted(list(result)): print(each)