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
start = 0 
end = max(trees)

while start <= end:
    middle = (start+end)//2
    wood = 0

    for i in trees:
        if i > middle:
            wood += i - middle
    
    if wood == m:
        end = middle
        break

    elif wood > m :
        start = middle +1

    else:
        end = middle -1

print(end)