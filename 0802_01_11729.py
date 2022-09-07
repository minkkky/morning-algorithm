# https://www.acmicpc.net/problem/11729


# n=원판의 개수, a=시작 장대1, b=목표 장대3, c=보조 장대2
def hanoi(n, a, b, c):
    if n == 1:
        print(a, b)

    else:
        hanoi(n-1, a, c, b)
        print(a, b)
        hanoi(n-1, c, b, a)

n = int(input())

print(2**n-1)
hanoi(n, 1, 3, 2)