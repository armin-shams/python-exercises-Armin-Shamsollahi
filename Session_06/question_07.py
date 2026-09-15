orders = [('Ali', 'Laptop'),
          ('Sara', 'Phone'),
          ('Ali', 'Phone'),
          ('Reza', 'Laptop'),
          ('Sara', 'Laptop'),
          ('Ali', 'Tablet'),
          ('Reza', 'Phone')]

my_dic = {}
for name, product in orders :
    if name in my_dic :
        my_dic[name].append (product)
    else :
        my_dic [name] = [product]
print(my_dic)