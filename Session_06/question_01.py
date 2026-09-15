products = {'laptop': 1200,
            'phone': 800,
            'tablet': 500,
            'headphone': 150,
            'mouse': 50}
max_product_price = 0
for i,j in products.items() :
    if j > max_product_price :
        max_product_price = j
        max_product_name = i
print ('The most expensive item is :',max_product_name)

min_product_price = float('inf')
for i,j in products.items() :
    if j < max_product_price :
        min_product_price = j
        min_product_name = i
print ('The cheapest item is :',min_product_name)

my_sum = 0
count = 0
for i,j in products.items() :
    my_sum += j
    count += 1
    ave = my_sum / count
print ('The average price of products is :',ave)
print ('The sum of all prices is :',my_sum)

print ('These items is more expensive than 500 :')
for i,j in products.items() :
    if j > 500 :
        print (j)


