d, p, q = map(int, input().split())

if p < q:
    p, q = q, p

div_p = d // p + 1
min_cost = div_p * p

if d % p == 0 or d % q == 0:
    min_cost = d
else:
    for i in reversed(range(div_p)):
        div_q, res_q = divmod(d - (i * p), q)
        if res_q == 0:
            min_cost = d
            break
        tmp = (i * p) + ((div_q + 1) * q)
        if tmp == min_cost:
            break
        min_cost = min(tmp, min_cost)
print(min_cost)
