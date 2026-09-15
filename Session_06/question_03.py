my_sent = input('Please enter your random sentence :\n').lower().strip().replace(' ','')
my_list = ['!', '@', '#', '$', '%', '^', '&', '*', '.', '+', '=']
my_dic = {}
for i in my_sent :
    if i in my_dic and i not in my_list :
        my_dic [i] += 1
    elif i not in my_dic and i not in my_list :
        my_dic [i] = 1
print(my_dic)