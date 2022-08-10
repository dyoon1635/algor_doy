num = int(input())
digit = [0] * 10
num1, num2, d = 0, 0, 1

while True:
    num1, num2 = num // (d * 10), num % (d * 10)
    if num1 == 0: break

    for i in range(10):
        digit[i] += num1 * d
    for i in range(1, num2 // d):
        digit[i] += d
    digit[num2 // d] += (num2 % d) + 1
    d *= 10
for i in range(1, num2 // d):
    digit[i] += d
digit[num2 // d] += (num2 % d) + 1
for idx, each in enumerate(list(reversed(str(num)))):
    if each == '0':
        digit[0] -= (10 ** idx)
for d in digit: print(d, end=' ')