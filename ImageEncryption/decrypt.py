from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from PIL import Image
import sys

def decrypt_image(input_path, output_path, key):
    with open(input_path, 'rb') as f:
        # Read header info
        mode_length = int.from_bytes(f.read(1), byteorder='big')
        img_mode = f.read(mode_length).decode()
        width = int.from_bytes(f.read(4), byteorder='big')
        height = int.from_bytes(f.read(4), byteorder='big')
        iv = f.read(16)
        encrypted_bytes = f.read()

    # Create AES cipher in CBC mode with the same IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt and unpad
    decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)

    # Create image from bytes
    img = Image.frombytes(img_mode, (width, height), decrypted_bytes)
    img.save(output_path)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python decrypt.py <input_encrypted_file> <output_image>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # AES key must match the encryption key
    key = b'pallaviSECURE123'  # Use the same key as in encryption

    decrypt_image(input_file, output_file, key)
    print(f"Image decrypted and saved to {output_file}")
