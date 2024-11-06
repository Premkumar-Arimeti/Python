class Account:
   def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc
   def debit(self,amount=100):
        self.bal-=amount
        print(amount, "is debited")
   def credit(self,amount=500):
        self.bal+=amount
        print(amount, "is credited")
   def get_balance(self):
        return self.bal
user=Account(1000,12345)
user.debit()
user.credit()
print(user.get_balance())