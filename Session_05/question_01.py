my_pass = input ('Please Enter your password:\n')
upper = False
lower = False
digit = False
special = False
if len (my_pass) >= 8 :
    for i in my_pass :
        if i.isupper() :
            upper = True
        if i.islower() :
            lower = True
        if i.isdigit() :
            digit = True
        if not i.isalnum():
            special = True
    if upper == False :
        print ('Password must contain at least 1 uppercase letter.')
    if lower == False :
        print ('Password must contain at least 1 lowercase letter.')
    if digit == False :
        print ('Password must contain at least 1 number.')
    if special == False :
        print ('Password must contain at least 1 special character.')
    if upper == True and lower == True and digit == True and special == True :
        print ('Your password set successfully.')
else :
    print ('Password must contain at least 8 characters.')