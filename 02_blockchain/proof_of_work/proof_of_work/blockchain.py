import json
import random
from datetime import datetime
from hashlib import sha256

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        print("Creating gensis block")
        self.new_block()

    def new_block(self):
        block = {
            'index': len(self.chain),
            'timestamp': datetime.utcnow().isoformat(),
            'transactions': self.pending_transactions,
            'previous_hash': self.last_block['hash'] if self.last_block else None,
            'nonce': format(random.getrandbits(64), "x")
        }

        block_hash = self.hash(block)
        block['hash'] = block_hash

        self.pending_transactions = []

        return block

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1] if self.chain else None

    def proof_of_work(self):
        while True:
            new_block = self.new_block()
            if self.valid_block(new_block):
                break
        self.chain.append(new_block)
        print("found new block: ", new_block)

    def valid_block(self, block):
        return block["hash"].startswith("0000")
