numbers = int(input('How many numbers do you want to enter ?\n'))
my_list = []
neg_list = []
while numbers <= 0 :
    print('The entry value must be positive.\n')
    numbers = int(input('How many numbers do you want to enter ?\n'))
for i in range(0, numbers) :
    x = int(input('Enter a number!\n'))
    my_list.append(x)
print(my_list)
for i in my_list:
    if i < 0 :
        neg_list.append(i)
print(neg_list)
        