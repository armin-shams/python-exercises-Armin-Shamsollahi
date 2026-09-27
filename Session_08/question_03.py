transactions = 'C://Users//IT CITY//Desktop//Github//Practice//python-exercises-Armin-Shamsollahi//Session_08//03 - transactions.txt'

def calculate_balance () :
    balance_dic = {}
    with open (transactions, 'r') as f :
        for info in f :
            person = info.strip().split(',')
            print(person)
            if person [1] == 'deposit' :
                if person [0] in balance_dic :
                    balance_dic [person[0]] += int(person [2])
                else :
                    balance_dic [person[0]] = int(person [2])
            elif person [1] == 'withdraw' :
                if person [0] in balance_dic :
                    if balance_dic [person[0]] >= int(person[2]) :
                        balance_dic [person[0]] -= int(person [2])
                else :
                    balance_dic [person[0]] = 0
    return balance_dic
                    
def total_deposits() :
    total_dep_dic = {}
    with open (transactions, 'r') as f :
        for info in f :
            person = info.strip().split(',')
            if person [1] == 'deposit' :
                if person [0] in total_dep_dic :
                    total_dep_dic [person[0]] += int(person [2])
                else :
                    total_dep_dic [person[0]] = int(person [2])
    return total_dep_dic

def total_withdrawals() :
    total_with_dic = {}
    with open (transactions, 'r') as f :
        for info in f :
            person = info.strip().split(',')
            if person [1] == 'withdraw' :
                if person [0] in total_with_dic :
                    total_with_dic [person[0]] += int(person [2])
                else :
                    total_with_dic [person[0]] = int(person [2])
    return total_with_dic

def find_invalid_transactions() :
    balance_dic = {}
    invalid_dic = {}
    with open (transactions, 'r') as f :
        for info in f :
            person = info.strip().split(',')
            if person [1] == 'deposit' :
                if person [0] in balance_dic :
                    balance_dic [person[0]] += int(person [2])
                else :
                    balance_dic [person[0]] = int(person [2])
            elif person [1] == 'withdraw' :
                if person [0] in balance_dic :
                    if balance_dic [person[0]] >= int(person[2]) :
                        balance_dic [person[0]] -= int(person [2])
                    else :
                        if person [0] in invalid_dic :
                            invalid_dic[person[0]].append(person)
                        else :
                            invalid_dic[person[0]] = [person]
                else :
                    balance_dic[person[0]] = 0
                    if person[0] in invalid_dic :
                        invalid_dic[person[0]].append(person)
                    else : 
                        invalid_dic[person[0]] = [person]
    return invalid_dic

def generate_report () :
    balances = calculate_balance()
    total_deposit = total_deposits()
    total_withdrawal = total_withdrawals()
    invalid_transactions = find_invalid_transactions()
    report = {}
    for user in balances :
        report [user] = {'name': user,
                         'total_deposit': total_deposit[user],
                         'total_withdrawal': total_withdrawal[user],
                         'balance': balances[user],
                         'invalid_transaction': invalid_transactions.get(user, [])}
    return report
            
print(generate_report())         