N = int(input())
Num = N
count = 0
while True:
    a = Num//10 #십의자리수
    b = Num%10 #일의자리수
    c = (a+b)%10 #십의자리수+일의자리수>일의자리수
    Num = (b*10)+c #새 숫자
    count += 1
    if Num == N:
        print(count)
        break