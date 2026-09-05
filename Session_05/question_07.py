my_sent = input ('Please Enter a sentence :\n').lower()
my_dic = {}
for i in my_sent :
    if i in my_dic :
        my_dic[i] +=1
    else :
        my_dic[i] = 1
for i, j in my_dic.items() :
        print (i,j, sep = '', end = '')