withdraw_amount = int(input('مبلغ برداشت وجه خود را وارد کنید:\n'))
account_balance = int(input('موحودی خود را وارد نمایید.\n'))
if withdraw_amount <= 0 :
    print('مبلغ برداشت میبایست مثبت باشد.')
else :
    if withdraw_amount < account_balance :
        res = account_balance - withdraw_amount
        print('عملیات برداشت با موفقیت انجام گردید.')
        print('موجودی باقی مانده ی شما :', res)
    else :
        print('موجودی حساب شما کافی نمی باشد.')
        