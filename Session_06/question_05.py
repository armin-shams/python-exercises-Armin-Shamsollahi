students = {'Ali':  [18, 17, 20],
            'Sara': [15, 19, 18],
            'Reza': [12, 14, 10],
            'Mina': [20, 20, 19]}
score_sum = 0
count = 0
highest_ave = 0
for i in students :
    scores = students[i]
    for score in scores :
        score_sum += score
        count += 1
    ave = score_sum / count
    if ave >= 15 :
        accept_status = 'Passed'
    else :
        accept_status = 'Failed'
    print(i)
    print(f'{ave:.2f}')
    print(accept_status,'\n')
    if ave > highest_ave :
        highest_ave = ave
        best_student = i
print(f'Best student is {best_student}.')
print(f'Highest average is {highest_ave:.2f}.')