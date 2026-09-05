my_str = input('Enter a sentence : \n')
alpha_count = 0
lower_count = 0
upper_count = 0
digit_count = 0
space_count = 0
char_count = 0
for i in my_str :
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
    else :
        char_count += 1
print ('letters :',alpha_count,'\n' 
       'lowercase :',lower_count,'\n'
       'Uppercase :',upper_count,'\n'
       'Digits :',digit_count,'\n'
       'Spaces :',space_count,'\n'
       'Special characters :',char_count)