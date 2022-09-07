# https://www.acmicpc.net/problem/3052

num = []

for i in range(10):
    num.append(int(input())%42)

print(len(set(num)))