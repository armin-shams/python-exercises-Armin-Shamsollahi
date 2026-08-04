record = 0
for i in range (1, 11) :
    new = int(input('Enter your height :\n'))
    if new > record :
        print('رکورد تازه ای ثبت شده است.')
        record = new
        print('بیشترین پرش تا این لحظه ثبت شد =',record,'متر')
    else : 
        print('این مقدار قبلا ثبت گردیده است.')
print('بالاترین ارتفاع ثبت شده =',record,'متر')
