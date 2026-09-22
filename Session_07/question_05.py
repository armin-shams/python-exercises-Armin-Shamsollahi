def login_count (logs) :
    success = 0
    fail = 0
    for log in logs :
        name, status, error = log
        if status == 'LOGIN' and error == 200 :
            success += 1
        elif status == 'LOGIN' and error == 403:
            fail += 1
    return success, fail

def check_suspicious_users (logs) :
    fail_login = {}
    suspicious_users = []
    for log in logs :
        name, status, error = log
        if error == 403 :
            if name in fail_login :
                fail_login[name] += 1
            else :
                fail_login[name] = 1
    for name , count in fail_login.items() :
        if count >= 3 :
            suspicious_users.append(name)
    return suspicious_users

def operations_count (logs) :
    operations = {}
    for log in logs :
        name, status, error = log
        if name in operations :
            operations [name] += 1
        else :
            operations [name] = 1
    return operations

def generate_report (logs) :
    success, fail = login_count(logs)
    suspicious_users = check_suspicious_users(logs)
    operations = operations_count(logs)
    report = {
    "successful_logins": success,
    "failed_logins": fail,
    "suspicious_users": suspicious_users,
    "operations": operations}
    return report

logs = [("Ali", "LOGIN", 200),
        ("Ali", "DOWNLOAD", 200),
        ("Sara", "LOGIN", 403),
        ("Reza", "LOGIN", 200),
        ("Sara", "LOGIN", 403),
        ("Sara", "LOGIN", 403)]

print (generate_report(logs))


