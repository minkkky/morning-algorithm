# https://www.acmicpc.net/problem/1929

# 에라토스테네스의 체 알고리즘
# https://coding-of-today.tistory.com/170?category=995820
import math

n = 1000000
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

x,y = map(int, input().split())
for i in range(x, y+ 1):
    if array[i]:
        print(i)