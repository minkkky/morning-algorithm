# https://www.acmicpc.net/problem/1037

n = int(input())
divisors = list(map(int, input().split()))

if n == 1:
    num = divisors[0]**2
else:
    num =  max(divisors)*min(divisors)

print(num)

