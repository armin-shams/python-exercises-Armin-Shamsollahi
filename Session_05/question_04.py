my_sent = input ('Enter your sentence : \n').lower()
my_list = my_sent.split(' ')
my_dic = {}
for i in my_list :
    if i in my_dic.keys() :
        my_dic [i] += 1
    else :
        my_dic [i] = 1
max_value = 0
for i, j in my_dic.items() :
    if j > max_value :
        max_value = j
        max_key = i
for i, j in my_dic.items() :
    if j == max_value :
        print(i,'---->',j)