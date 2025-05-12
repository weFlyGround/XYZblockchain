#init class for transactions
class Transaction:
    def __init__(self, sender, recipient, amount, miner_address, fee = 1):
        self.sender = sender
        self.recipient = str(recipient)
        self.amount = amount
        self.with_fee = (self.amount * fee) / 100
        self.miner_address = miner_address
        self.fee = (amount * fee) / 100
