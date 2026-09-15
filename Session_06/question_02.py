inventory = {'apple': 20,
             'banana': 5,
             'orange': 0,
             'milk': 12,
             'bread': 0}
available_list = []
out_of_stock_list = []
count_available = 0
count_out_of_stock = 0
for i, j in inventory.items() :
    if j == 0 :
        out_of_stock_list.append(i)
        count_out_of_stock += 1
    else :
        available_list.append(i)
        count_available += 1
print('out of stock products are :',out_of_stock_list)
print('available products are :',available_list)
print(f'There are {count_out_of_stock} products out of stock.')
print(f'There are {count_available} products available.')