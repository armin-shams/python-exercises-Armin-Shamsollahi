legal_func = ['subtraction', '-', 'tafrigh', 'menha'\
              ,'zarb', '*', 'multiply', 'ضرب', 'sum'\
              ,'+', 'jam', 'جمع','به علاوه', 'تفریق' ,'منها'\
              ,'division', '/', 'taghsim', 'تقسیم']
mul_func = ['zarb', '*', 'multiply', 'ضرب']
sum_func = ['sum', '+', 'jam', 'جمع', 'به علاوه']
sub_func = ['subtraction', '-', 'tafrigh', 'menha', 'تفریق' ,'منها']
div_func = ['division', '/' , 'taghsim', 'تقسیم']

num1 = int(input('Enter first number : \n'))
num2 = int(input('Enter second number : \n'))
user_func = input('What mathematical operation would you like to perform ? \n')

while user_func not in legal_func :
    print('Your operation is not a mathematical operation!, try again\n')
    num1 = int(input('Enter first number : \n'))
    num2 = int(input('Enter second number : \n'))
    user_func = input('What mathematical operation would you like to perform ? \n')
if user_func in mul_func :
    my_res = num1 * num2
elif user_func in sum_func :
    my_res = num1 + num2
elif user_func in sub_func :
    my_res = num1 - num2
else :
    my_res = num1 / num2
    
print('Result = ',my_res)
