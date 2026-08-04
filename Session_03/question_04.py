#method 1
x = input('write your sentence!\n')
x_len = len(x)
if x_len % 2 == 0 :
    print(x[:(x_len//2)])
else :
    print(x[(x_len//2):])
'''
#method 2
x = input('write your sentence!\n')
x_len = 0
for i in x :
    x_len += 1
c = x_len // 2
if x_len % 2 == 0 :
    print(x[:c])
else :
    print(x[c:])
        '''