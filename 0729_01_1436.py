# https://www.acmicpc.net/problem/1436

n = int(input())

num = []
base = "666"
cnt = 1

while len(num) < n:
    if base in str(cnt):
        num.append(cnt)
        cnt += 1
    else:
        cnt += 1

print(num[n-1])

# for i in range(n):
#     num.append(i*1000+base)
#     num.append(int(str(base)+str(i)))
#     set(num)
#     num.sort()

# title_num = num[n-1]
# print(title_num)
# print(len(num))
# print(num.index(title_num))

