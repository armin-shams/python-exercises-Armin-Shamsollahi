my_sent = input ('Enter your sentence : \n').lower()
my_list = my_sent.split(' ')
my_dic = {}
max_len = 0
for i in my_list :
    if i in my_dic.keys() :
        my_dic [i] += 1
    else :
        my_dic [i] = 1
for i, j in my_dic.items() :
    if len(i) > max_len :
        max_len = len(i)
        max_key = i
print (max_key,'\nLength :',max_len)