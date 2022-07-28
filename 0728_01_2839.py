# https://www.acmicpc.net/problem/2839

sugars = int(input())
q = 0

while sugars >= 0:

    if sugars % 5 == 0: #5의배수
        q += sugars // 5
        print(q)
        break

    sugars -= 3
    q += 1

else:
    print(-1)

'''
루프문(for, else)은 else 절을 가질 수 있습니다.

루프가 이터러블의 소진이나 (for의 경우) 
조건이 거짓이 돼서 (while의 경우) 종료할 때 실행됩니다. 

하지만 루프가 break 문으로 종료할 때는 실행되지 않습니다.

참고: https://docs.python.org/ko/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
'''

'''첫 시도 (실패)
if r == 0:
    print(q)

elif r == 3:
    print(q+1)
    
else:
    q = sugars // 3
    r = sugars % 3

    if r == 0:
        print(q)

    else:
        print(-1)
'''

