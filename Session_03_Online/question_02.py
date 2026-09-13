# question_02_a :
for i in range (30, 51) :
    if i % 2 != 0 :
        print(i)
        
#question_02_b :
count = 0
for i in range (30, 7000) :
    if i % 2 != 0 :
        count += 1
print('number of odd numbers is :',count)

#question_02_c :
even_list = []
for i in range (60, 120) :
    if i % 2 == 0 :
        even_list.append(i)
print('even list =',even_list) 
    