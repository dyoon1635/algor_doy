target = int(input())
n = int(input())
broken = [] # 망가진 button
if n != 0: # 망가진 button이 없으면 추가 입력 x
    broken = list(map(int, input().split()))

def brute_force(eps):
    # eps = 1이면 찾을때까지 channel을 올림
    # eps = -1이면 찾을때까지 channel을 내림
    count = 0
    if target == 100: return 0

    cur_channel = target # 목표 channel에서 출발
    while True:
        # 0 <= N <= 5e+5 이므로 upper bound = 1e+6으로 설정
        if cur_channel > 1000000 or cur_channel < 0:
            return 1000000

        tmp = str(cur_channel)
        check = True
        # 현재 channel에 button을 눌러 접근 가능한지 check
        for i in range(len(tmp)):
            if int(tmp[i]) in broken:
                check = False

        if check: return len(tmp) + count
        cur_channel += eps
        count += 1

if __name__ == "__main__":
    print(min(brute_force(1),
              brute_force(-1),
              abs(100 - target)))