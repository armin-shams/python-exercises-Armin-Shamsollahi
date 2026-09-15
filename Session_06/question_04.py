employees = {'E01':{'name': 'Ali',
                   'age': 28,
                   'salary': 3000},
             'E02':{'name': 'Sara',
                    'age': 32,
                    'salary': 4500},
             'E03':{'name': 'Reza',
                    'age': 25,
                    'salary': 2800}}
max_salary = 0
for employee in employees.values() :
    if employee ['salary'] > max_salary :
        max_salary = employee ['salary']
        max_salary_employee = employee ['name']
print(f'{max_salary_employee} has the highest salary between employees.')

min_salary = float ('inf')
for employee in employees.values() :
    if employee ['salary'] < min_salary :
        mix_salary = employee ['salary']
        mix_salary_employee = employee ['name']
print(f'{mix_salary_employee} has the lowest salary between employees.')

my_sum = 0
count = 0
for employee in employees.values() :
    my_sum += employee ['salary']
    count += 1
    ave = my_sum // count
print(f'The average salary amount is {ave}.')

print ('These employees earn more than 3000 salary :')
for employee in employees.values() :
    if employee ['salary'] > 3000 :
        print(employee['name'])