def is_prime_num(n):
    n = int(n)
    if n <= 1: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

def count_number(num):
    cnt, tmp = 0, ''
    prime_set = set()
    for ch in num:
        if ch == '0':
            if tmp and is_prime_num(tmp):
                cnt += 1
            tmp = ''
        else:
            tmp += ch
    if tmp and is_prime_num(tmp): cnt += 1
    return cnt

def radix(n, k):
    res, div = '', 1

    while div < n: div *= k
    div /= k

    while div != 1:
        res += str(int(n // div))
        n %= div
        div /= k
    return res + str(int(n))

def solution(n, k):
    return count_number(radix(n, k))