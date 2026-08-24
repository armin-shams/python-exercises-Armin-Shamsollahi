import random

my_list = ['سنگ', 'قیچی' , 'کاغذ']
print('بازی سنگ ،کاغذ ،قیچی\n\n\n')
print ('سنگ ، کاغذ، قیچی')

while True :
    x = input('انتخاب کن!\n')

    if x == 'exit' :
        print('هر وقت دوس داشتی بیا بازی کنیم.')
        break
    if x not in my_list :
        print ('ورودی میبایست سنگ یا کاغذ یا قیچی باشد.')
        continue
    
    ran_game = random.choice(my_list)
    print('انتخاب من :', ran_game)

    if x == ran_game :
        print ('هر دو مساوی شدیم\n')
    elif (x == 'سنگ'  and ran_game == 'قیچی') or \
         (x == 'کاغذ'  and ran_game == 'سنگ') or \
         (x == 'قیچی'  and ran_game == 'کاغذ') :
        print ('آفرین، شما برنده شدید.\n')
    else :
        print ('متاسفانه شما باختید!\n')
