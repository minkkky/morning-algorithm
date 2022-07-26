def d(n):
    num = n
    for i in str(n):
        num += int(i)
    return num

n = 10000

not_self_num = []

for i in range(n):
   not_self_num.append(d(i))

for a in range(n):
    if a in not_self_num:
        pass
    else:
        print(a)