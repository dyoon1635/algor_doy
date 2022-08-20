A, T = input(), input()
rA = A[::-1]
front, back = [], []
lp, rp, length = 0, len(T) - 1, len(A)

while lp <= rp:
    while lp <= rp:
        front.append(T[lp])
        lp += 1
        if len(front) >= length and ''.join(front[-length:]) == A:
            del front[-length:]
            break
    while lp <= rp:
        back.append(T[rp])
        rp -= 1
        if len(back) >= length and ''.join(back[-length:]) == rA:
            del back[-length:]
            break

result = front + back[::-1]
while True:
    tmp = ''.join(result)
    idx = tmp.find(A)
    if idx == -1: break
    del result[idx : idx + length]
print(''.join(result))
