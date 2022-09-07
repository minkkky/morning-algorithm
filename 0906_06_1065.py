# https://www.acmicpc.net/problem/1065

hansu_list = []

for i in range(1, 1001):
    if i <= 99:
        hansu_list.append(i)
    else:
        a = i//100
        b = i%100//10
        c = i%100%10
        if a - b == b -c :
            hansu_list.append(i)

num = int(input())

cnt = 0
for i in hansu_list:
    if i <= num:
        cnt += 1

print(cnt)