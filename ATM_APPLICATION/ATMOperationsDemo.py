#main program
from ATMMenu import menu
from ATMOperations import Deposite,Withdraw,Balenq
from ATMExceptions import DepositeError,WithdrawError,InsufficentFundError
while(True):
    try:
        menu()
        ch = int(input("Enter Your Choice:"))

        match ch:
            case 1:
                try:
                    Deposite()
                except ValueError:
                    print("Do not enter alnums,symbols,strs for choice")
                except DepositeError:
                    print("Do not deposite zero or negative value")
            case 2:
                try:
                    Withdraw()
                except ValueError:
                    print("Do not enter alnums,symbols,strs for choice")
                except WithdrawError:
                    print("Do not withdraw zero or negative value")
                except InsufficentFundError:
                    print("your account have insufficentfund")


            case 3:
                Balenq()
            case 4 :
                print("Thanx For Using Our Atm Program")
                break
            case _:
                print("Your Choise Of Selection is Wrong ...Try Again!!")
    except ValueError :
        print("Do not enter alnums,symbols,strs for choice")