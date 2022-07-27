crotia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
string = input()
string_length = len(string)
crotia_cnt = 0

for c in crotia:
    if c == 'z=':
        z_cnt = string.count(c)-string.count("dz=")
        string_length -= z_cnt*len(c)
        crotia_cnt += z_cnt
    else:
        string_length -= string.count(c)*len(c)
        crotia_cnt += string.count(c)

print(string_length+crotia_cnt)




'''

if "-" in string:
    print("c-, d-")
    if "c-" in string:
        pass

if "=" in string:
    print("c=, s=, z=")

if "j" in string:
    print("lj, nj")

if "d" in string:
    print("dz, d-")

'''