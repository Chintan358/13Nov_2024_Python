
class InSufficientAmountException(Exception):
        def __init__(self,amt):
            print("Insufficent amount :",amt)

class Bank : 
    bal = 0

    def __init__(self):
        pass
    
    def get_balance(self):
        print("Your currentbalance is : ",self.bal)

    def deposite(self, amt):
        self.bal = self.bal+amt

    def withdrow(self, amt):
        if amt > self.bal :
            raise InSufficientAmountException(amt-self.bal)
        else : 
            self.bal = self.bal-amt

b = Bank()
b.get_balance()
b.deposite(1000)
b.deposite(5000)
b.get_balance()
try : 
    b.withdrow(100000)
except Exception :
    pass
b.get_balance()