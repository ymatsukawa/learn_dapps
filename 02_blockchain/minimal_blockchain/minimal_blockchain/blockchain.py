import json
from datetime import datetime
from hashlib import sha256

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        print("Creating gensis block")
        self.new_block()

    def new_block(self, previous_hash=None):
        block = {
            'index': len(self.chain),
            'timestamp': datetime.utcnow().isoformat(),
            'transactions': self.pending_transactions,
            'previous_hash': previous_hash
        }

        block_hash = self.hash(block)
        block['hash'] = block_hash

        self.pending_transactions = []
        self.chain.append(block)

        return block

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    def last_block(self):
        return self.chain[-1] if self.chain else None

    def new_transaction(self, sender, recipent, amount):
        self.pending_transactions.append({
            "sender": sender,
            "recipent": recipent,
            "amount": amount
        })
