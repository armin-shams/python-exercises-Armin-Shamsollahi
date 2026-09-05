remain_atempts = 3
while remain_atempts > 0 :
    my_user_name = input('Enter your username :\n')
    my_password = input('Enter Your password :\n')
    if my_user_name == 'armin.shams' and \
        my_password == 'Armin@1369' :
        print ('Login successful')
        break
    else : 
        remain_atempts -= 1
        print ('Wrong username or password')
        if remain_atempts == 0 :
            print ('Unfortunately your account has been locked,for help please contact admin team.')
        else :
            print ('Attempts remaining :',remain_atempts)