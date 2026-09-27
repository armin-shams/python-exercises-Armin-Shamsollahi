def get_values() :
    question_num = int(input ('How many values do you want to enter ?\n'))
    my_list = []
    for i in range(question_num) :
        value = input('Enter your favourite name :\n')
        my_list.append(value)
    return my_list

def add_unique(value, unique_list) :
    for i in unique_list :
        if value.lower() == i.lower() :
            return False
    unique_list.append(value)
    return True

def process_values() :
    unique_list = []
    duplicate_list = []
    lower_values = []
    values = get_values()
    for value in values :
        lower_values.append(value.lower())
    for value in values :
        if value == '' :
            print('Enter a name')
        else :
            is_new = add_unique(value, unique_list)
            if is_new == True :
                print(f'New enterance has added to list -> {value}')
            else :
                duplicate_list.append(value)
                position = lower_values.index(value.lower()) + 1
                print (f'{value} -> repetetive value,first enterance is {position}.')
    return unique_list, len(unique_list), len(duplicate_list), values

def show_report() :
    unique_list, unique_count, duplicate_count, values = process_values()
    print('unique values:',unique_list)
    print('number of duplicate values:',duplicate_count)
    print('number of unique values:',unique_count)
    print('\nfirst enterance :')
    lower_values = []
    for value in values :
        lower_values.append(value.lower())
    for value in unique_list :
        position = lower_values.index (value.lower()) + 1
        print (f'first enterance of {value} is {position}.')
        
show_report()