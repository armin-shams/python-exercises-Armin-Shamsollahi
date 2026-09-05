import random

ran_num = random.randint(0,100)
num = int(input('Make your guess between 0 to 100 :\n'))

while num not in range (0,101) :
    print('Your number is not in range.')
    num = int(input('Make your guess between 0 to 100 :\n'))
    
while num != ran_num :
    if ran_num < num :
        print('Your number is bigger.')
        num = int(input('make another guess :\n'))
    elif ran_num > num :
        print('Your number is smaller.')
        num = int(input('make another guess :\n'))
print('Congradulations.\n'
      "You've made it.\n"
      'GOOD GUESS.')
