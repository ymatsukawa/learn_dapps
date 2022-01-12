from hashlib import sha256

image = open('bird.png', 'rb')
hash_1 = sha256(image.read()).hexdigest()
image.close()

image = open('bird_other.png', 'rb')
hash_2 = sha256(image.read()).hexdigest()
image.close()

print(hash_1 != hash_2)
