import json
import hashlib

from time import time
from flask import Flask
from uuid import uuid4

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

