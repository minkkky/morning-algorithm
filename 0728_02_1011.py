# Fly me to the Alpha Centauri
# https://www.acmicpc.net/problem/1011

# 절반으로 나눠서 앞은 커지고 뒤는 작아지는 로직이어야 하나...?
# print(m/2, m//2, m%2)
# 참고: https://ooyoung.tistory.com/91

loop_cnt = int(input())

for i in range(loop_cnt):
    x, y = map(int, input().split(' '))
    d = y-x # 이동거리
    cnt = 0 # 이동회수
    mp = 1 # 이동가능거리
    mp_plus = 0 # 이동한 거리의 합
    
    while mp_plus < d :
        cnt += 1
        mp_plus += mp
        if cnt % 2 == 0:
            mp += 1

    print(cnt)