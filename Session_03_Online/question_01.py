my_pass = input('Please Enter your password : \n')
lower = False
upper = False
digit = False
if len(my_pass) >= 8 :
    for i in my_pass :
        if i.isdigit() :
            digit = True
        if i.isalpha() :
            alpha = True
        if i.islower() :
            lower = True          
        if i.isupper() :
            upper = True
    if upper == False :
        print ('Password must contain at least 1 uppercase letter.')
    if lower == False :
        print ('Password must contain at least 1 lowercase letter.')
    if digit == False :
        print ('Password must contain at least 1 number.')
    if upper == True and lower == True and digit == True :
        print ('Your password set successfully.')
else :
    print('Password must contains atleast 8 characters.')
