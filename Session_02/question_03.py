first = input('Enter Your first name!\n')
last = input('Enter your last name!\n')

if first[0:2] == 'sh' or first[0:2] == 'zh' or first[0:2] =='kh' :
    first_name = first[0:2].capitalize()
else :
    first_name = first[0].capitalize()
last_name = last.capitalize()

print(first_name,'.',last_name, sep='')
