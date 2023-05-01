import sys, heapq
input = sys.stdin.readline
MOD = 10 ** 9 + 7

for _ in range(int(input())):
    n = int(input())
    energy = list(map(int, input().split()))
    heapq.heapify(energy)
    total = 1
    while len(energy) > 1:
        slime1, slime2 = heapq.heappop(energy), heapq.heappop(energy)
        total *= (slime1 * slime2) % MOD
        heapq.heappush(energy, slime1 * slime2)
    print(total % MOD)