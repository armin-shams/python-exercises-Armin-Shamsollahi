x = input('Enter your passcode :\n'
          'Your passcode must consist 2 parts.\n'
          'first part contains 4 letter and second part contains 4 digit.\n')
if len(x) != 8 :
    print ('Your pass is invalid.')
else :
    if x[0:4].isalpha() and x[4:8].isdigit():
            print('Your passcode is valid.')
    else :
        print('Your passcode is invalid.')
            