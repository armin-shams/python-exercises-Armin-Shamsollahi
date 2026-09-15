products = {'P01': ('Laptop', 1200, 5),
            'P02': ('Phone', 800, 0),
            'P03': ('Tablet', 500, 12),
            'P04': ('Mouse', 50, 25),
            'P05': ('Keyboard', 100, 0)}

print ('available products :')
for code, (name, price, stock) in products.items() :
    if stock > 0 :
        print (name)

print ('\nout of stock products :')
for code, (name, price, stock) in products.items() :
    if stock == 0 :
        print (name)

print ('\ntotal value of every product based on its stock is :')
total_value_warehouse = 0
highest_value = 0
for code, (name, price, stock) in products.items () :
    total_value = stock * price
    print (name,'----->',total_value)
    total_value_warehouse += total_value
    
    if total_value > highest_value :
        highest_value = total_value
        highest_value_product = [name]
    elif total_value == highest_value:
        highest_value_product.append(name)

print('\nThe most valuable products are :')
for name in highest_value_product :
    print (name)
print ('\ntotal warehouse value is :',total_value_warehouse)
