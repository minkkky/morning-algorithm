H, M = map(int, input().split(' ')) # H시 M분

if M >= 45:
    print(f'{H} {M-45}')
else:
    if H == 0:
        print(f'23 {M-45+60}')
    else:
        print(f'{H-1} {M-45+60}')