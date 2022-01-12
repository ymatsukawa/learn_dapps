import hashlib

input_1 = b"helloworld"
output_1 = hashlib.sha256(input_1)
print(output_1.hexdigest())

input_2 = b"Helloworld"
output_2 = hashlib.sha256(input_2)
print(output_2.hexdigest())

input_3 = b"Helloworld"
output_3 = hashlib.sha256(input_3)
print(output_3.hexdigest())

print(output_1.hexdigest() != output_2.hexdigest())
print(output_2.hexdigest() == output_3.hexdigest())
