# custom exp

class LowBalanceExceptionCustom(Exception):

    def __init__(self,message):
        self.messsage = message
        super().__init__(message)


        balance = 100
        withdraw = int(input("enter the amount you want to withdraw"))
        if withdraw > balance:
            raise LowBalanceExceptionCustom("Balance is low")
        else:
            print("Remain Bal",(balance - withdraw))