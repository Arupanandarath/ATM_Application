from ATMExceptions import DepositeError,WithdrawError,InsufficentFundError
bal = 500
def Deposite():
    global bal
    damt = float(input("Enter how much money you want to deposite:"))
    if(damt<=0):
        raise DepositeError
    else:
        bal=bal+damt
        print("your account ********5123 credited with {}".format(damt))
        print("your current balance is {}".format(bal))

def Withdraw():
    global bal
    wamt=float(input("enter how much amount you want to debit:"))
    if(wamt<=0):
        raise WithdrawError
    elif((wamt + 500)>bal):
        raise InsufficentFundError
    else:
        bal=bal-wamt
        print("your account *********5123 debited with{}".format(wamt))
        print("your current balance is {}".format(bal))

def Balenq():
    print("Your account *********5123 bal INR:{}".format(bal))