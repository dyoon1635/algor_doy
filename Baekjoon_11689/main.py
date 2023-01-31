while True:
    n = int(input())
    if n == 0: break
    result = n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result / i
    if n > 1: result -= result / n
    print(int(result))