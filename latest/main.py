import threading
from pynput import keyboard

from Blockchains import Blockchain
from functions import start_mining_loop, on_press, save_transactions_to_file
from json_chain import Chain_data
from Wallet import Wallet

if __name__ == "__main__":
        #blockchain and wallet init
        my_blockchain = Blockchain()
        miner_wallet = Wallet()

        #start mining thread
        mining_thread = threading.Thread(target=start_mining_loop, args=(my_blockchain,))
        mining_thread.start()

        #listen for "q" to stop the mining
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

        #checking is blockchain valid
        is_valid = my_blockchain.is_chain_valid()
        print("Is blockchain valid?", is_valid)

        #print transactions
        print("\nTransactions after mining:")
        for block in my_blockchain.chain:
            print(f"\nBlock {block.index}:")
            print(f"Hash: {block.hash}")
            print(f"Previous hash: {block.previous_hash}")
            print("Transactions:")
            for tx in block.transactions:
                if tx.sender == "System":
                    print(f"  Reward -> {tx.recipient}: {tx.amount}")
                    miner_wallet.plus_balance(tx.fee)
                else:
                    print(f"  {tx.sender} -> {tx.recipient}: {tx.amount} (Fee: {tx.fee})")

        #printing all miner's balance
        print(f"\nMiner's total earnings: {float(miner_wallet.balance)} tokens\n")

        #save transactions and chains to files
        save_transactions_to_file(my_blockchain)
        write_chains = Chain_data(my_blockchain)
        write_chains.create_json()
