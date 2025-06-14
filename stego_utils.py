import numpy as np

def encode_message(img, secret_bytes):
    flat = img.flatten()

    # Encode length in first 32 bits
    length = len(secret_bytes)
    length_bits = format(length, '032b')

    # Convert secret to bits
    secret_bits = ''.join(format(byte, '08b') for byte in secret_bytes)

    full_bits = length_bits + secret_bits

    if len(full_bits) > len(flat):
        raise ValueError("Image is too small to hold the secret message!")

    for i in range(len(full_bits)):
        flat[i] = (flat[i] & ~1) | int(full_bits[i])

    return flat.reshape(img.shape)

def decode_message(img):
    flat = img.flatten()

    # Decode the length (first 32 bits)
    length_bits = ''.join([str(flat[i] & 1) for i in range(32)])
    length = int(length_bits, 2)

    # Now extract the message
    message_bits = [str(flat[i] & 1) for i in range(32, 32 + length * 8)]
    byte_list = [int(''.join(message_bits[i:i+8]), 2) for i in range(0, len(message_bits), 8)]
    
    return bytes(byte_list)
