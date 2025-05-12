import hashlib
import time

#init class for one block in blockchain
class Block:
    def __init__(self, index, previous_hash, transactions, timestamp=None, nonce=0):
        #init self in class for appealing a class designators
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.calculate_hash()

    #calculating hash based on self designators
    def calculate_hash(self):
        block_content = f"{self.index}{self.previous_hash}{self.timestamp}{[tx.__dict__ for tx in self.transactions]}{self.nonce}"
        return hashlib.sha256(block_content.encode()).hexdigest()
    
    #mining block with the Proof of Work
    def mine_block(self):
        target = "abc"
        while target not in self.hash:
            self.nonce += 1
            self.hash = self.calculate_hash()
            print(f"Mining... Nonce: {self.nonce}, Hash: {self.hash}")
