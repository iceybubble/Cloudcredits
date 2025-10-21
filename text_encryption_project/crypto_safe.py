from cryptography.fernet import Fernet
import hashlib
import os


def generate_key():
    """
    Generate and save a new Fernet encryption key.
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("New encryption key generated and saved as 'key.key'.")


def load_key():
    """
    Load an existing encryption key from key.key file.
    """
    if not os.path.exists("key.key"):
        print("Key not found! Please generate one first (Option 1).")
        return None
    with open("key.key", "rb") as key_file:
        return key_file.read()


def encrypt_text(message):
    """
    Encrypt plain text using the loaded Fernet key.
    """
    key = load_key()
    if key is None:
        return
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    print("\nEncrypted text:")
    print(encrypted.decode())
    with open("encrypted_data.txt", "wb") as enc_file:
        enc_file.write(encrypted)
    print("Encrypted text saved to 'encrypted_data.txt'.")


def decrypt_text():
    """
    Decrypt encrypted text using the Fernet key.
    """
    key = load_key()
    if key is None:
        return
    if not os.path.exists("encrypted_data.txt"):
        print("No encrypted file found! Please encrypt something first.")
        return
    with open("encrypted_data.txt", "rb") as enc_file:
        encrypted = enc_file.read()
    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(encrypted).decode()
        print("\nDecrypted text:")
        print(decrypted)
    except Exception:
        print("Decryption failed. Invalid key or corrupted file.")


def hash_text(text):
    """
    Generate a SHA256 hash of the input text (one-way encryption).
    """
    hashed = hashlib.sha256(text.encode()).hexdigest()
    print("\nSHA256 Hash (One-Way):")
    print(hashed)


def menu():
    while True:
        print("""
====================================
CRYPTO SAFE — TEXT ENCRYPTION TOOL
====================================
1. Generate Encryption Key
2. Encrypt Text
3. Decrypt Text
4. Hash Text (SHA256)
5. Exit
""")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            generate_key()
        elif choice == "2":
            msg = input("Enter text to encrypt: ")
            encrypt_text(msg)
        elif choice == "3":
            decrypt_text()
        elif choice == "4":
            text = input("Enter text to hash: ")
            hash_text(text)
        elif choice == "5":
            print("Exiting Crypto Safe. Stay secure!")
            break
        else:
            print("Invalid choice. Please enter a number between 1–5.")


if __name__ == "__main__":
    menu()
