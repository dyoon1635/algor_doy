t, a = input(), list(input())
length = len(a)
res = []
for each in t:
    res.append(each)
    if len(res) >= length and res[-length:] == a:
        del res[-length:]

if not res: print('FRULA')
else:
    for each in res:
        print(each, end='')
    print('')
