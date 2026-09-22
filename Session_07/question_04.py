def check_large_transaction(transaction) :
    name, transaction_type, amount, time = transaction
    if amount > 100000000 :
        return True
    else :
        return False
    
def check_repeated_withdrawals(transactions) :
    withdraw_count = 0
    suspicious_transactions = []
    for transaction in transactions :
        name, transaction_type, amount, time = transaction
        if transaction_type == 'withdraw' :
            withdraw_count += 1
            if withdraw_count > 3 :
                suspicious_transactions.append(transaction)
        else :
            withdraw_count = 0   
    return suspicious_transactions

def check_balance(transactions) :
    balances = {}
    suspicious_transactions = []
    for transaction in transactions :
        name, transaction_type, amount, time = transaction
        if name not in balances :
            balances[name] = 0
        if transaction_type == 'deposit' :
            balances[name] += amount
        elif transaction_type == 'withdraw' :
            balances[name] -= amount
            if balances[name] < 0 :
                suspicious_transactions.append(transaction)
    return suspicious_transactions
     
def generate_fraud_report (transactions) :      
    fraud_report = []
    for transaction in transactions :
        if check_large_transaction(transaction) :
            fraud_report.append(transaction)
    balance_fraud = check_balance(transactions)
    if balance_fraud :
        fraud_report.extend(balance_fraud)
    repeated_frauds = check_repeated_withdrawals(transactions)
    fraud_report.extend(repeated_frauds)
    return fraud_report

def detect_fraud(transactions) :
    fraud_report = generate_fraud_report(transactions)
    return fraud_report
    
transactions = [('Ali', 'deposit', 50000000, 10),
                ('Ali', 'withdraw', 2000000, 11),
                ('Ali', 'withdraw', 3000000, 12),
                ('Ali', 'withdraw', 4000000, 13),
                ('Ali', 'withdraw', 5000000, 14),
                ('Ali', 'withdraw', 6000000, 15),
                ('Sara', 'deposit', 50000000, 20),
                ('Sara', 'withdraw', 60000000, 21),
                ('Reza', 'deposit', 150000000, 30)]

print(detect_fraud(transactions))
    
    
