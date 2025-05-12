import json

#chain data class init
class Chain_data:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    #creating json blockchain information
    def create_json(self, filename="block_chain.json"):
        chain_data = []
        for block in self.blockchain.chain:
            block_data = {
                "block": block.index,
                "previous_hash": block.previous_hash,
                "transactions": [ 
                    {"sender": tx.sender, "recipient": tx.recipient, "amount": tx.amount, "with fee": tx.with_fee}
                    for tx in block.transactions
                ],
                "timestamp": block.timestamp,
                "nonce": block.nonce,
                "hash": block.hash,
            }
            chain_data.append(block_data)

        with open(filename, "w") as json_file:
            json.dump({"chain": chain_data}, json_file, indent=4)

        print("Blockchain information successfully saved to", filename)
