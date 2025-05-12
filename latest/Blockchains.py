from Transactions_class import Transaction
from Blocks import Block

class Blockchain:
    #initialization of the blockchain
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []

    #genesis block (the first of an all blockchain)
    def create_genesis_block(self):
        return Block(0, "xyz", [])

    #takes the latest block in chain
    def get_latest_block(self):
        return self.chain[-1]

    #appending transactions to queue
    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    #appending transactions right now
    def mine_pending_transactions(self, miner_address, amount):
        reward_transaction = Transaction("System", recipient=miner_address, miner_address=miner_address, amount=amount)
        self.pending_transactions.append(reward_transaction)

        new_block = Block(
            index=len(self.chain),
            previous_hash=self.get_latest_block().hash,
            transactions=self.pending_transactions
        )

        print("Mining started...")
        new_block.mine_block()
        print("Block mined:", new_block.hash)

        self.chain.append(new_block)
        self.pending_transactions = []
    
    #cheking is chain valid
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True
