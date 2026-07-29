x = int(input('Enter your purchase amount!\n'))

if x > 1000000 :
    x = x * 0.85
elif 500000 <= x <= 1000000 :
    x = x * 0.9
    
print(int(x))
