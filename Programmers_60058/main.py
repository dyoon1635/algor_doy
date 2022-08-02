def check(u):
    s = []
    for c in u:
        if c == ')':
            if s and s[-1] == '(':
                s.pop()
            else:
                s.append(c)
        else:
            s.append(c)
    if s: return False
    return True

def solution(p):
    answer = ''
    if not p: return answer
    open_cnt, close_cnt = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            open_cnt += 1
        else:
            close_cnt += 1

        if open_cnt == close_cnt:
            u = p[:i + 1]
            v = p[i + 1:]
            break
    if check(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        for c in u[1: len(u) - 1]:
            if c == '(':
                answer += ')'
            else:
                answer += '('
    return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
