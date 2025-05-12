from functions import miner_id

#init wallet
class Wallet:
    def __init__(self):
        #get miner id and class init
        self.address = miner_id()
        self.balance = 0
    #plus the balance by fee
    def plus_balance(self, fee):
        self.balance += fee
