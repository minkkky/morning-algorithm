# https://www.acmicpc.net/problem/25304

X = int(input())
N = int(input())
cart = 0

for i in range(N):
    price, count  = map(int, input().split())
    cart += price * count

if cart == X:
    print("Yes")
else:
    print("No")
