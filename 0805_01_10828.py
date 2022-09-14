# https://www.acmicpc.net/problem/10828

stack = []

loop_cnt = int(input())

for i in range(loop_cnt):

    t = list(map(int, input().split()))
    order = t[0]

    if t[1]:
        value = t[1]

    if order == "push":
        stack.append(value)
    
    if order == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            p = stack.pop(-1)
            print(p)

    if order == "size":
        print(len(stack))
    
    if order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    if order == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    
    print(stack)
