distance = float(input('مسافت را بر اساس کیلومتر وارد نمایید.\n'))
if distance > 2 :
    diff = int(distance - 2)
    taxi_fare = 20000 + (5000 * diff)
else :
    taxi_fare = 20000
    
print(int(taxi_fare))
