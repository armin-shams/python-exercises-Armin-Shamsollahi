time = int(input('Enter the hour!\n'))

if time > 23 or time < 0 :
    print('بازه ی ساعتی بین 0 تا 23 را وارد نمایید.')
elif 5 <= time <= 10 :
    print('صبح')
elif 10 < time <= 14 :
    print('ظهر')
elif 14 < time <= 19 :
    print('عصر')
else :
    print ('شب')
    