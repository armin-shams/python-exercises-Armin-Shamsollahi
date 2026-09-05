my_sent = input ('Please Enter a sentence :\n').lower()
my_list = my_sent.split(' ')
my_limit_list = ['hack', 'fraud', 'scam', 'password', 'attack']
my_dic = {}
for i in my_list :
    if i in my_dic :
        my_dic[i] +=1
    else :
        my_dic[i] = 1
for i, j in my_dic.items() :
    if i in my_limit_list :
        print (i,'---->',j)