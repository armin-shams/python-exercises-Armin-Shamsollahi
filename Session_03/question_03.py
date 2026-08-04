sum1 = 0
sum2 = 0
for i in range (1, 11):
    if i % 2 == 0:
        res = i + 5
        sum1 = sum1 + res
        print(i ,'+ 5 =',res)
    else :
        res = i * 5
        sum2 = sum2 + res
        print (i ,'* 5 =',res )
sum3 = sum1 + sum2
print('The sum of all operation is',sum3,'.')
        