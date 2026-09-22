def analyze_transactions (transactions) :
    info = {}
    for name, transaction_type, amount in transactions :
        if name not in info :
            info [name] = {'deposits': 0,
                           'withdrawals': 0,
                           'balance_change': 0,
                           'transactions': 0}
        if transaction_type == 'deposit' :
            info[name]['deposits'] += amount
            info[name]['balance_change'] += amount
            info[name]['transactions'] += 1
        elif transaction_type == 'withdraw' :
            info[name]['withdrawals'] += amount
            info[name]['balance_change'] -= amount
            info[name]['transactions'] += 1
    max_deposit = 0
    max_withdraw = 0
    max_transaction = 0
    max_with_person = ''
    max_dep_person = ''
    max_transaction_person = ''
    for name, data in info.items() :
        if data['deposits'] > max_deposit :
            max_deposit = data['deposits']
            max_dep_person = name
        if data['withdrawals'] > max_withdraw :
            max_withdraw = data['withdrawals']
            max_with_person = name
        if data['transactions'] > max_transaction :
            max_transaction = data['transactions']
            max_transaction_person = name
    return {'person_informaiton' : info,
            'max_deposit' : max_dep_person,
            'max_withdraw': max_with_person,
            'most_active' : max_transaction_person}
transactions = [
    ('Ali', 'deposit', 5000000),
    ('Ali', 'withdraw', 1000000),
    ('Sara', 'deposit', 8000000),
    ('Ali', 'withdraw', 500000),
    ('Sara', 'withdraw', 2000000),
    ('Reza', 'deposit', 10000000)]

print (analyze_transactions(transactions))