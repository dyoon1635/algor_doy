def out_of_bound(x, l):
    if x < 0 or x >= l: return True
    return False

def solution(s):
    length = len(s)
    arr = list(s)

    if length == 1: return 1

    answer = 1
    for eps in [0, 1]: # palindrome 길이가 홀수, 짝수인 경우 보정 상수
        for i in range(length - 1):
            # res, eps 보정.
            res, start, end = 1 + eps, i, i + eps
            if arr[start] != arr[end]: continue

            for j in range(end, length):
                end, gap = end + 1, end - start + 1 - eps
                if out_of_bound(end, length) or \
                        out_of_bound(start - gap, length):
                    break

                if arr[start - gap] == arr[end]: res += 2
                else: break
            answer = max(answer, res)
    return answer