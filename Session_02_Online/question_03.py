x = input('Do you want to make an order ?\n')
if x.lower().replace(' ','') == 'yes' :
    print('You are welcome :\n'
          'We are at your service')
elif x.lower().replace(' ','') == 'no' :
    print("It's Ok, as you wish.")
else :
    print("'Please just answer with 'yes' or 'no'")
    