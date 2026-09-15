users = [('Ali', 25, 'Python'),
         ('Sara', 30, 'Java'),
         ('Reza', 22, 'Python'),
         ('Mina', 28, 'C++'),
         ('John', 35, 'Python'),
         ('David', 30, 'Java')]

my_language = {}
for name, age, language in users :
    if language in my_language :
        my_language [language].append(name)
    else :
        my_language [language] = [name]
print(my_language)
    
groups = {}
for user in users :
    name = user [0]
    age = user [1]
    language = user [2]
    
    if language not in groups :
        groups [language] = []
    groups [language].append ((name, age))
for language, group in groups.items() :
    sum = 0
    count = 0
    for user in group :
        sum += user [1]
        count += 1
    ave = sum // count
    print (language, ave)

old_age = 0
old_user = ''
for user in users :
    if user [1] > old_age :
        old_age = user [1]
        old_user = user [0]
print(f'Oldest user is {old_user}.')

max_user = 0
max_language = ''

for language, group in groups.items():
    if len(group) > max_user :
        max_user = len(group)
        max_language = language
print (f'{max_language} has the most user.')





