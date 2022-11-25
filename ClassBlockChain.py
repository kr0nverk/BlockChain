import json
import hashlib

from time import time
from flask import Flask
from uuid import uuid4
from flask import jsonify, request

class Blockchain(object):
    def __init__(self):
        self.current_transactions = []
        self.chain = []

        # First Block
        self.new_block(previous_hash=1, prof=100)


    def new_block(self, prof, previous_hash):
        # Add new block

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transaction': self.current_transactions,
            'prof': prof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        # Add new transaction

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # Hash of block

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # Return last block
        return self.chain[-1]


    def prof_of_work(self, last_prof):
        # PoW
        prof = 0

        while self.prof_valid(last_prof, prof) is False:
            prof += 1

        return prof

    @staticmethod
    def prof_valid(last_prof, prof):
        #

        x = f'{last_prof}{prof}'.encode()
        x_hash = hashlib.sha256(x).hexdigest()
        return x_hash[:5] == "00000"
