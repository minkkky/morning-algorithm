# https://www.acmicpc.net/problem/2609
# 최대공약수 최소공배수

a, b = map(int, input().split(' '))

a_li = []
b_li = []
cnt = 0

if a <= b :
    min = a
    max = b
else:
    min = b
    max = a

while cnt < min:
    cnt += 1

    if a % cnt == 0 :
        a_li.append(cnt)

    if b % cnt == 0 :
        b_li.append(cnt)

c = 0 

for i in a_li:
    if i in b_li:
        c = i

print(c) # 최대공약수

cnt = 0

while True:
    cnt += 1
    if min * cnt % max == 0:
        print(min * cnt) # 최소공배수
        break