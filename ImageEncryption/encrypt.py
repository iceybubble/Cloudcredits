from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from PIL import Image
import sys

def encrypt_image(input_path, output_path, key):
    # Open image and convert to bytes
    with Image.open(input_path) as img:
        img_bytes = img.tobytes()
        img_mode = img.mode
        img_size = img.size

    # Generate a random IV
    iv = get_random_bytes(AES.block_size)

    # Create AES cipher in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Pad and encrypt image bytes
    encrypted_bytes = cipher.encrypt(pad(img_bytes, AES.block_size))

    # Save encrypted data with header info (mode, size, iv)
    with open(output_path, 'wb') as f:
        # Save mode and size as header for decryption
        f.write(len(img_mode).to_bytes(1, byteorder='big'))
        f.write(img_mode.encode())
        f.write(img_size[0].to_bytes(4, byteorder='big'))
        f.write(img_size[1].to_bytes(4, byteorder='big'))
        f.write(iv)
        f.write(encrypted_bytes)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <input_image> <output_encrypted_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # AES key must be either 16, 24, or 32 bytes long
    key = b'pallaviSECURE123'  # Replace with secure key management in real projects

    encrypt_image(input_file, output_file, key)
    print(f"Image encrypted and saved to {output_file}")
