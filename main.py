from time import time


class Blockchain(object):
    def __int__(self):
        self.chain = []
        self.current_transaction = []
        self.new_block()

    def new_block(self):
        # Add new block

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transaction': self.current_transaction,
            'proof': proof,
            'previous_hash': self.hash(self.chain[-1]),
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
        pass

    def last_block(self):
        # Return last block
        return self.chain[-1]


#def create_first_block():
#
#    block_deta = {}
#    block_deta['index'] = 0
#    block_deta['timestsmp'] = datetime.datetime.now()
#    block_deta['data'] = 'First Data'
#    block_data['proof'] = proof
#    block_deta['prev_hash'] = None
#
#    block = Block(block_deta)
#    return block

if __name__ == '__main__':
    create_first_block()

