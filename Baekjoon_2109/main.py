n = int(input())
course = []
for _ in range(n):
    course.append(list(map(int, input().split()))) # p, d
# 1 <= day <= 1e+4
# total_pay는 idx날에 얻을 수 있는 maximum pay를 의미
total_pay = [0] * 10001
course.sort(key=lambda x: (-x[0])) # order by pay desc

for pay, day in course:
    for i in reversed(range(1, day + 1)):
        if pay > total_pay[i]:
            total_pay[i] = pay
            break
print(sum(total_pay))