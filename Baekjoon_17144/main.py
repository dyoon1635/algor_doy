import copy

r, c, t = map(int, input().split())
room = []
for _ in range(r):
    room.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def printf():
    for row in room: print(row)

def out_of_bound(x, y):
    if x < 0 or x >= r or y < 0 or y >= c:
        return True
    return False

def count_dust():
    # 남아있는 미세먼지 양 count
    total = 2 # air conditioner 값 보정
    for row in room:
        total += sum(row)
    return total

def get_cond_loc(): # air conditioner pos return
    for i in range(r):
        for j in range(c):
            if room[i][j] == -1:
                return (i, j)

def diffusion():
    global room
    tmp = copy.deepcopy(room)
    for x in range(r):
        for y in range(c):
            # if there is no dust or air conditioner
            if room[x][y] <= 0: continue

            count = 0
            dust = room[x][y] # 현재 위치 dust 양
            diff_dust = int(dust / 5) # 현재 위치에서 퍼져나갈 dust 양
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not out_of_bound(nx, ny) \
                        and room[nx][ny] != -1:
                    tmp[nx][ny] += diff_dust
                    count += 1
            tmp[x][y] -= (count * diff_dust)
    room = tmp

def purify(eps, x, y):
    # eps = 1 이면 counter clockwise 정화
    # epo = -1 이면 clockwise 정화
    dir = 3
    cur_x, cur_y = x, y # air conditioner에서 출발
    while True:
        nx, ny = cur_x + dx[dir], cur_y + dy[dir]
        if out_of_bound(nx, ny) or nx == x + eps:
            dir = (dir + eps) % 4
            nx, ny = cur_x + dx[dir], cur_y + dy[dir]
        if room[cur_x][cur_y] != -1:
            if room[nx][ny] != -1:
                room[cur_x][cur_y] = room[nx][ny]
            else:
                room[cur_x][cur_y] = 0
        cur_x, cur_y = nx, ny
        # air conditioner로 돌아오면 break
        if room[cur_x][cur_y] == -1: break

def conditioner():
    cond_x, cond_y = get_cond_loc()
    purify(1, cond_x, cond_y)
    purify(-1, cond_x + 1, cond_y)

if __name__ == "__main__":
    for _ in range(t):
        diffusion()
        conditioner()
        #printf()
    print(count_dust())

