import heapq

if __name__ == "__main__":
    n, k = map(int, input().split())
    jewel = []
    bags = []
    for _ in range(n):
        heapq.heappush(jewel, list(map(int, input().split())))
    for _ in range(k):
        heapq.heappush(bags, int(input()))

    res = 0
    tmp = []
    for _ in range(k):
        w = heapq.heappop(bags)
        while jewel and jewel[0][0] <= w:
            m, v = heapq.heappop(jewel)
            heapq.heappush(tmp, -v)
        if tmp: res -= heapq.heappop(tmp)
        elif not jewel: break
    print(res)

