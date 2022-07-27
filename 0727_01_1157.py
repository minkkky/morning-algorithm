string = str(input())
string = string.upper()
set_string = set(string)

string_cnt = []
string_cnt_dict = {}

for s in set_string:
    d = []
    d.append(s)
    count = string.count(s)
    d.append(count)
    string_cnt.append(d)
    
string_cnt_dict.update(string_cnt)
sorted_dict = sorted(string_cnt_dict.items(), key = lambda item: item[1], reverse = True)

if len(sorted_dict) == 1:
    print(sorted_dict[0][0])
else:
    if sorted_dict[0][1] == sorted_dict[1][1]:
        print("?")
    else:
        print(sorted_dict[0][0])

   
    '''
string = str(input())
set_string = set(string)

string_cnt = []
string_cnt_dict = {}

for s in set_string:
    d = []
    d.append(s)
    count = string.count(s)
    d.append(count)
    string_cnt.append(d)
    
string_cnt_dict.update(string_cnt)
sorted_dict = sorted(string_cnt_dict.items(), key = lambda item: item[1], reverse = True)

if sorted_dict[0][1] == sorted_dict[1][1]:
    print("?")
else:
    print(sorted_dict[0][0])

    '''