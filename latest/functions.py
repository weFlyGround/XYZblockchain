import os
import random
import time
from Transactions_class import Transaction

# global bool variable for stopping the program
stop_mining = False

# Create an ID for miner if it does not exist and save to .txt
def miner_id():
    filename = "miner_id.txt"
    miner_address = ""

    # Check if the file exists
    if not os.path.exists(filename):
        # Create the file and generate a new miner ID
        with open(filename, "w", encoding="utf-8") as file:
            miner_address = str(random.getrandbits(32))
            file.write(miner_address)
    else:
        # Read the existing miner ID
        with open(filename, "r", encoding="utf-8") as file:
            miner_address = file.read().strip()

    return miner_address

# Start mining pool
def start_mining_loop(blockchain):
    global stop_mining
    miner_address = miner_id()  # Ensure miner ID is loaded or created
    while not stop_mining:
        sender = random.getrandbits(32)
        recipient = random.getrandbits(32)
        amount = random.randint(1, 50)
        
        blockchain.add_transaction(Transaction(sender, recipient, amount, miner_address))
        blockchain.mine_pending_transactions(miner_address, amount=amount)
        
        time.sleep(1)

# Listen for press "q" key
def on_press(key):
    global stop_mining
    try:
        if key.char == "q":
            stop_mining = True
            print("\nStop mining...")
            return False
    except AttributeError:
        pass

# Saving transactions to .txt
def save_transactions_to_file(blockchain, filename="transactions.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Transactions from blockchain:\n")
        for block in blockchain.chain:
            if block.index == 0:
                file.write(f"\nBlock {block.index}: Genesis block\n")
            else:
                file.write(f"\nBlock {block.index}:\n")
            for tx in block.transactions:
                if tx.sender == "System":
                    file.write(f"  ID: {tx.sender} -> ID: {tx.recipient}: {tx.fee};\n")
                else:
                    file.write(f"  ID: {tx.sender} -> ID: {tx.recipient}: {tx.amount};\n")
    print(f"Transactions information successfully saved to {filename}.")
