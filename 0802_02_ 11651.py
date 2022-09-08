# https://www.acmicpc.net/problem/11651

n = int(input())
dots = []

for i in range(n):
    a, b = map(int, input().split())
    dots.append((a, b))

sorted_dots = sorted(dots, key=lambda x: (x[1], x[0]))

for i in range(n):
    print(f'{sorted_dots[i][0]} {sorted_dots[i][1]}')