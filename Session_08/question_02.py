log = 'C://Users//IT CITY//Desktop//Github//Practice//python-exercises-Armin-Shamsollahi//Session_08//02 - logs.txt'

def count_successful_logins() :
    count = 0
    with open (log, 'r') as f :
        for info in f :
            person = info.strip().split(',')
            if person [2] == '200' :
                if person [1] == 'LOGIN' :
                    count += 1
    return count
                    
def count_failed_logins() :
    count = 0
    with open (log, 'r') as f :
        for info in f :
            person = info.strip().split(',')
            if person [2] == '500' or person [2] == '403' :
                if person [1] == 'LOGIN' :
                    count += 1
    return count

def find_suspicious_users() :
    user_dic = {}
    susp_list = []
    with open (log, 'r') as f :
        for info in f :
            person = info.strip().split(',')
            if person [2] == '403' :
                if person [0] not in user_dic :
                    user_dic [person[0]] = 1
                else :
                    user_dic [person[0]] += 1
        for user, count in user_dic.items() :
            if count >= 3 :
                susp_list.append(user)
    return susp_list    

def generate_report() :
    operation = {}
    with open (log, 'r') as f :
        for info in f :
            person = info.strip().split(',')
            if person [0] in operation :
                operation [person[0]] += 1
            else :
                operation [person[0]] = 1
    successful_logins = count_successful_logins()
    failed_logins = count_failed_logins()
    suspicious_users = find_suspicious_users()
    
    report = {'successful_logins' : successful_logins,
              'failed_logins' : failed_logins,
              'suspicious_users' : suspicious_users,
              'operations' : operation}
    return report

print (generate_report())