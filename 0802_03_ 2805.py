# https://www.acmicpc.net/problem/2805

'''시간초과 > 이분탐색 써야할듯

n, m = map(int, input().split())
trees = list(map(int, input().split()))

h = max(trees)

while h >= 0:

    h -= 1
    t = 0

    for i in rangetrees:
        if i > h:
            t += i - h

    if t >= m:
        print(h)
        break
'''

n, m = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)

while start <= end:
    middle = max(trees)//2
    wood = 0

    for i in trees:
        if i > middle:
            wood += i - middle

    if wood >= m :
        start = middle +1

    else:
        end = middle -1

print(wood)
print(start, end)
print(end)