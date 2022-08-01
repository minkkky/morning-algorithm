# https://www.acmicpc.net/problem/10250

t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())

    num = n//h +1
    floor = n%h*100

    if n%h == 0: # 나누어떨어질때
        num = n//h
        floor = h*100

    print(floor+num)