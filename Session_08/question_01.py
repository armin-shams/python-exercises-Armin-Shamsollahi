users = 'C://Users//IT CITY//Desktop//Github//Practice//python-exercises-Armin-Shamsollahi//Session_08//01 - users.txt'
def find_user(username) :
    with open (users, 'r') as f :
        for info in f :
            person = info.replace(' ','').strip().split(',')
            if person [0] == username :
                return person[1], person[2]

def add_user(username, password, status) :
    existing_user = find_user(username)
    if existing_user is not None :
        print('User already exists.')
    else :
        with open (users, 'a') as f :
            f.write (f'{username}, {password}, {status}\n')
            
def delete_user (username) :
    user_info = []
    with open (users, 'r') as f :
        for info in f :
            person = info.replace(' ','').strip().split(',')
            if person [0] != username :
                user_info.append(person)
    with open(users, 'w') as f :
        for person in user_info :
            line = ','.join(person)
            f.write(line +'\n')
            
def generate_report() :
    active = 0
    blocked = 0
    with open (users, 'r') as f :
        for info in f :
            person = info.replace(' ','').strip().split(',')
            if person [2] == 'active' :
                active += 1
            elif person [2] == 'blocked' :
                blocked += 1
        print (f'{active} users are active & {blocked} users are blocked')

generate_report()
add_user('Sara', 12345, 'active')
print(find_user('Sara'))