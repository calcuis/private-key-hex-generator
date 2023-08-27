import random

def generate_private_key():
    # Generate a random 32-byte (256-bit) private key
    private_key = random.getrandbits(256)
    return private_key

private_key = generate_private_key()
print("Generated Private Key:", hex(private_key)[2:])
