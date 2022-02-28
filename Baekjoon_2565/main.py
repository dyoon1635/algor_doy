n = int(input())
cord = []
for i in range(n):
    cord.append(list(map(int, input().split())))

if __name__ == "__main__":
    cord.sort()
    lis=[1] * n
    for i in range(n):
        for j in range(i):
            if cord[j][1] < cord[i][1] and lis[i] < lis[j] + 1:
                lis[i] = max(lis[i], lis[i] + 1)
    print(n - max(lis))