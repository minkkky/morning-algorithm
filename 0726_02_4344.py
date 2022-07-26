loop_cnt = int(input())

def sum(scores):
    result = 0
    for i in scores:
        result += i
    return result

def avg_up_students(students_cnt, scores, avg):
    up_stusent = 0
    for i in scores:
        if i > avg:
            up_stusent += 1
    result = up_stusent/students_cnt*100
    return result

for i in range(loop_cnt):
    input_data = input()
    slice_cnt = int(input_data.split(' ')[0])
    scores = list(map(int, input_data.split(' ')[1:slice_cnt+1]))
    sum_result = sum(scores)
    avg = sum_result/slice_cnt
    avg_up = avg_up_students(slice_cnt, scores, avg)

    print(f'{avg_up:.3f}%')