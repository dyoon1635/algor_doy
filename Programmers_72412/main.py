import heapq
from bisect import bisect_left
def lang_idx(lan):
    if lan == 'cpp':
        return [0]
    elif lan == 'java':
        return [1]
    elif lan == 'python':
        return [2]
    return [0, 1, 2]


def category_idx(category):
    if category == 'backend':
        return [0]
    elif category == 'frontend':
        return [1]
    return [0, 1]


def career_idx(career):
    if career == 'junior':
        return [0]
    elif career == 'senior':
        return [1]
    return [0, 1]


def food_idx(food):
    if food == 'chicken':
        return [0]
    elif food == 'pizza':
        return [1]
    return [0, 1]


def solution(info, query):
    result = [[[[[] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(3)]
    for record in info:
        lan, category, career, food, score = record.split()
        x, y = lang_idx(lan)[0], category_idx(category)[0]
        z, w = career_idx(career)[0], food_idx(food)[0]
        #print(lan, category, career, food, score)
        #print(x, y, z, w)
        #heapq.heappush(result[x][y][z][w], int(score))
        result[x][y][z][w].append(int(score))
    for x in range(3):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if result[x][y][z][w]:
                        result[x][y][z][w].sort()

    answer = []
    for record in query:
        cnt = 0
        each = record.split()

        x_idx, y_idx = lang_idx(each[0]), category_idx(each[2])
        z_idx, w_idx = career_idx(each[4]), food_idx(each[6])
        threshold = int(each[-1])
        print(record)
        #print(x_idx, y_idx, z_idx, w_idx)
        for x in x_idx:
            for y in y_idx:
                for z in z_idx:
                    for w in w_idx:
                        length = len(result[x][y][z][w])
                        if length:
                            left = bisect_left(result[x][y][z][w], threshold)
                            cnt += (length - left)

        answer.append(cnt)
    return answer

info = ["java backend junior pizza 100",
        "java backend junior pizza 0",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]
print(solution(info, query))
