import json
import hashlib

from time import time


class Blockchain(object):
    def __int__(self):
        self.chain = []
        self.current_transaction = []

        # First Block
        self.new_block(previous_hash=1, prof=100)


    def new_block(self, prof, previous_hash=None):
        # Add new block

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transaction': self.current_transaction,
            'prof': prof,
            'previous_hash': self.hash(self.chain[-1]) or previous_hash,
        }

        self.current_transaction = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        # Add new transaction

        self.current_transaction.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    def hash(block):
        # Hash of block

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


    def last_block(self):
        # Return last block
        return self.chain[-1]


    def prof_of_work(self, last_prof):
        # PoW
        prof = 0

        while self.prof_valid(last_prof, prof) is False:
            prof += 1

        return prof

    def prof_valid(last_prof, prof):
        #

        x = f'{last_prof}{prof}'.encode()
        x_hash = hashlib.sha256(x).hexdigest()
        return x_hash[:4] == "0000"
