📂 Project Structure
````
text_encryption_project/_
│
├── crypto_safe.py          # Main program for encryption, decryption, and hashing
├── encrypted_data.txt      # Stores encrypted text
└── key.key                 # Stores the Fernet encryption key
```

🔐 Overview

Crypto Safe is a Python-based text encryption tool designed to secure sensitive text data using Fernet symmetric encryption and SHA-256 hashing.
It provides an easy-to-use menu-driven interface that allows you to:

Generate and store encryption keys

Encrypt and decrypt text

Perform one-way hashing

This project is perfect for learning the fundamentals of cryptography, hashing, and secure key management in Python.

⚙️ Features

✅ Generate a new Fernet encryption key
✅ Encrypt and decrypt messages securely
✅ Create SHA-256 hashes for one-way text protection
✅ Save encrypted data to a file (encrypted_data.txt)
✅ Simple command-line menu-based interface

🧰 Requirements

You need Python 3.8+ and the cryptography library.

Install it using pip:
```
pip install cryptography
```
🚀 How to Use

Run the program:
```
python crypto_safe.py
```

You’ll see this interactive menu:
```
====================================
CRYPTO SAFE — TEXT ENCRYPTION TOOL
====================================
1. Generate Encryption Key
2. Encrypt Text
3. Decrypt Text
4. Hash Text (SHA256)
5. Exit
```
```
🧩 Option 1 – Generate Encryption Key
```
Creates a new Fernet encryption key and saves it as key.key.

> Enter choice: 1
New encryption key generated and saved as 'key.key'.
```
🔒 Option 2 – Encrypt Text
```
Encrypts your text input using the saved Fernet key.

> Enter choice: 2
Enter text to encrypt: Hello World
Encrypted text:
gAAAAABm...
Encrypted text saved to 'encrypted_data.txt'.
```
🔓 Option 3 – Decrypt Text
```
Decrypts previously encrypted data from encrypted_data.txt using key.key.

> Enter choice: 3
Decrypted text:
Hello World


If the key is missing or corrupted, you’ll see:

Decryption failed. Invalid key or corrupted file.
```
🔑 Option 4 – Hash Text (SHA256)
```
Generates a one-way SHA-256 hash of any text you enter.

> Enter choice: 4
Enter text to hash: password123
SHA256 Hash (One-Way):
ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
```
🏁 Option 5 – Exit
```
Safely exits the program.

⚠️ Important Notes

Keep key.key private — anyone with it can decrypt your data.

SHA-256 hashing is irreversible — once hashed, it cannot be decrypted.

Make sure encrypted_data.txt and key.key are in the same directory when decrypting.

🧠 Technologies Used

Python 3

cryptography (Fernet symmetric encryption)

hashlib (SHA256 hashing)

os (File handling utilities)