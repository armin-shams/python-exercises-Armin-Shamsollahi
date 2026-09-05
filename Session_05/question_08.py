my_str = input('Enter a sentence : \n')
total_char_count = 0
alpha_count = 0
lower_count = 0
upper_count = 0
digit_count = 0
space_count = 0
for i in my_str :
    total_char_count += 1
    if i.isalpha():
        alpha_count += 1
        if i.islower() :
            lower_count += 1
        else :
            upper_count += 1
    elif i.isdigit() :
        digit_count += 1
    elif i.isspace() :
        space_count += 1

my_dic1 = {}
num_rep_char = 0
for i in my_str :
    if i in my_dic1 and i != ' ':
        my_dic1[i] += 1
    else :
        my_dic1[i] = 1
for i, j in my_dic1.items() :
    if j > num_rep_char :
        num_rep_char = j
        most_rep_char = i

my_list = my_str.split(' ')
my_dic2 = {}
num_rep_word = 0
for i in my_list :
    if i in my_dic2 :
        my_dic2[i] += 1
    else :
        my_dic2[i] = 1
for i, j in my_dic2.items() :
    if j > num_rep_word :
        num_rep_word = j
        most_rep_word = i
        
max_len = 0
min_len = 999999
for i in my_dic2.keys() :
    if len(i) > max_len :
        max_len = len(i)
        long_word = i
    if len(i) < min_len and i != ' ' :
        min_len = len(i)
        short_word = i
        
print ('Total characters :',total_char_count,'\n'
       'Total letters :',alpha_count,'\n' 
       'Total digits :',digit_count,'\n'
       'Total spaces :',space_count,'\n'
       'Total uppercase :',upper_count,'\n'
       'Total lowercase :',lower_count,'\n'
       'Longest word :',long_word,'\n'
       'Shortest word :',short_word,'\n'
       'Most repeated character :',most_rep_char,'\n'
       'Most repeated word :',most_rep_word)