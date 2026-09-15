sales = (('Ali', 'Laptop', 1200),
         ('Sara', 'Phone', 800),
         ('Ali', 'Phone', 800),
         ('Reza', 'Laptop', 1200),
         ('Sara', 'Laptop', 1200),
         ('Ali', 'mouse', 50))
my_dic1 = {}
for customer, product, price in sales :
    if customer in my_dic1 :
        my_dic1 [customer] += price
    else :
        my_dic1 [customer] = price

total_sales = 0
highest_sales_number = 0
for costumer, total_price in my_dic1.items() :
    print(costumer,'---->',total_price)
    total_sales += total_price
    if total_price > highest_sales_number:
        highest_sales_number = total_price
        highest_sales_person = costumer

my_dic2 = {}
for customer, product, price in sales :
    if product in my_dic2 :
        my_dic2 [product] += 1
    else :
        my_dic2 [product] = 1

highest_number_sales = 0
for product, number_sales in my_dic2.items() :
    print(f'{product} has been sold {number_sales} times.') 

print(f'{highest_sales_person} is the top buyer.')
print('Total sales:',total_sales)