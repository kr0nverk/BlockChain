import json
import hashlib

from time import time
from flask import Flask
from uuid import uuid4
from flask import jsonify, request

from ClassBlockChain import Blockchain


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

app = Flask(__name__)

node_id = str(uuid4()).replace('-', '')

blockchain = Blockchain()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/mine', methods=['GET'])
def mine():


    last_block = blockchain.last_block
    last_prof = last_block['prof']
    prof = blockchain.prof_of_work(last_prof)

    blockchain.new_transaction(
        sender="0",
        recipient=node_id,
        amount=1,
    )

    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(prof, previous_hash)

    response = {
        'message': "New Block Add",
        'index': block['index'],
        'transaction': block['transaction'],
        'prof': block['prof'],
        'previous_hash': block['previous_hash'],
    }

    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():

    val = request.get_json()

    if not all(k in val for k in ['sender', 'recipient', 'amount']):
        return "Error in val", 400

    index = blockchain.new_transaction(val['sender'], val['recipient'], val['amount'])

    response = {'message': f'Add to blockchain{index}'}

    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def chains():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

