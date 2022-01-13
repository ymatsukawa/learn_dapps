from hashlib import sha256


def hash_with_secret(data, phrase):
    mixed_data = data + phrase
    return sha256(mixed_data.encode()).hexdigest()

secret_phrase = "this is our secret phrase!"
received_data = """It's been a while. I send you 0.0001 BTC.
Plz verify this text with secret and hash
I told in other message.
"""
# hash from "It's been while" is 74bd8f670d5887ff4c5f3aa1398ee8663d5d07eadaa706707c433a704ca9203f
received_hash = "74bd8f670d5887ff4c5f3aa1398ee8663d5d07eadaa706707c433a704ca9203f"
hashed = hash_with_secret(received_data, secret_phrase)
# equal. It's not tempered
print(hashed == received_hash)
