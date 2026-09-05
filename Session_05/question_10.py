my_sent_1 = input ('Please Enter first sentence : \n').lower()
my_sent_2 = input ('Please Enter second sentence : \n').lower()
my_list_1 = my_sent_1.split(' ')
my_list_2 = my_sent_2.split(' ')
print ('Common words :')
for i in my_list_1 :
    if i in my_list_2 :
        print(i)