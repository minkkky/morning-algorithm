# 베르트랑 공준
# https://www.acmicpc.net/problem/4948

import math

n = 246912
array = [True for i in range(n + 1)]
primary_num = []

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(2, n + 1):
    if array[i]:
        primary_num.append(i)

while n != 0:
    n = int(input())
    res = 0

    if n == 0:
        break

    for i in primary_num:
        if n < i <= 2*n:
            res += 1

    print(res)
