x = input('Please Enter your name and ID nummber.\n'
          'for example : Armin0520204301.\n')
id_num = int(x[-10:])

'''
Because of int() function that has mentioned in question , 
zero will removed in id cards with 0 in beginnings.
'''

print(id_num)
