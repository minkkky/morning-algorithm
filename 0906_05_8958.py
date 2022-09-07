# https://www.acmicpc.net/problem/8958

N = int(input())
tests = []

for i in range(N):
    tests.append(list(input()))

for j in tests:
    score = 1
    result = 0
    for x in range(len(j)):
        if j[x] == 'O':
            if x > 0:
                if j[x-1] == j[x]:
                    score += 1
            result += score
        else:
            score = 1
    print(result)