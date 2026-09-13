product_list = ['Shirt','T-shirt','Jeans','Coats']
while True :
    x = input('Do you want to add new product ?\n')
    if x.lower().replace(' ','') == 'yes' :
        p = input("Please enter product's name :\n")
        if p not in product_list :
            product_list.append(p.capitalize().replace(' ',''))
            print(product_list)
    elif x.lower().replace(' ','') == 'no':
        print("It's Ok, as you wish.")
        break
else :
    print("'Please just answer with 'yes' or 'no'")
