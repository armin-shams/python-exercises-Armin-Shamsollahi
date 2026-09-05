my_sent = input ('Please Enter a sentence :\n')
my_list = []
for i in my_sent :
    if i not in my_list :
        my_list.append(i)
my_sent_new = ''.join (my_list)
print(my_sent_new)