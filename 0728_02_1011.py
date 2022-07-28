# Fly me to the Alpha Centauri
# https://www.acmicpc.net/problem/1011

loop_cnt = int(input())
cnt = 0

for i in range(loop_cnt):
    x, y = map(int, input().split(' '))
    m = y-x # 이동거리
    # 절반으로 나눠서 앞은 커지고 뒤는 작아지는 로직이어야 하나...?