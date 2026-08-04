print('Please write colors in English.\n')
col_1 = input('write your favourite color #1 :\n')
col_2 = input('write your favourite color #2 :\n')
col_3 = input('write your favourite color #3 :\n')
col1 = col_1.replace(' ', '')
col2 = col_2.replace(' ', '')
col3 = col_3.replace(' ', '')

if col1.lower() == col2.lower() == col3.lower() :
    print('سه رنگ یکسان هستند.')
elif col1.lower() == col2.lower() or \
     col2.lower() == col3.lower() or \
     col1.lower() == col3.lower() :
    print('دو رنگ یکسان هستند.')
else :
    print('رنگ ها یکسان نیستند.')
