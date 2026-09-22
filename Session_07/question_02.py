def process_order (customer, *products, **options):
    discount = options.get('discount', 0)
    tax = options.get('tax', 0)
    shipping = options.get('shipping', 0)
    total_price = 0
    for i in products :
        total_price += prices [i]
    discount_price = (total_price * discount) // 100
    tax_price =  ((total_price - discount_price) * tax) // 100
    final_price = (total_price - discount_price) + tax_price + shipping
    
    return {'customer': customer,
            'products': products,
            'discount': discount,
            'tax': tax,
            'shipping': shipping,
            'final_price': final_price}
prices = {'Laptop': 1200000,
          'Mouse': 500000,
          'Keyboard': 60000}
print(process_order('Ali', 'Laptop' ,'Mouse', 'Keyboard',
                    discount = 10, tax = 9, shipping = 200000))