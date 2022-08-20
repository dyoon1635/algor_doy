from collections import deque
f, s, g, u, d = map(int, input().split())
visited = [False] * (f + 1)
visited[0], visited[s] = True, True

def out_of_bound(x):
    if x > f or x < 1: return True
    return False

def bfs():
    dq = deque()
    dq.append([s, 0]) # location, move
    while dq:
        loc, mov = dq.popleft()
        #print(loc, mov)
        if loc == g:
            print(mov)
            return None

        if not out_of_bound(loc + u) and not visited[loc + u]:
            visited[loc + u] = True
            dq.append([loc + u, mov + 1])
        if not out_of_bound(loc - d) and not visited[loc - d]:
            visited[loc - d] = True
            dq.append([loc - d, mov + 1])
    print('use the stairs')
bfs()