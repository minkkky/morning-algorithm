# 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

n = int(input())
cnt = n

for i in range(n):
    word = input()
    for j in range(0, len(word)-1):
        # print(word[j])
        # print(word[j+1])
        # print(word[j+1:])
        if word[j] ==  word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)