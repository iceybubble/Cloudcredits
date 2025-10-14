                                          Image Encryption Project

Overview

This project implements an image encryption and decryption tool using the AES symmetric key cryptographic algorithm. The tool secures digital images by encrypting pixel data, ensuring confidentiality during storage or transmission.

Features:

Encrypt and decrypt images in popular formats like PNG and JPG.

Uses AES encryption in CBC mode for strong security.

Supports encryption and accurate decryption with the correct secret key.

Easy-to-use command-line interface for processing images.

Project Structure

```
ImageEncryption/
│
├── encrypt.py          # Script to encrypt images  
├── decrypt.py          # Script to decrypt images  
├── README.md           # This file  
├── requirements.txt    # Python dependencies  
└── sample_images/      # Sample images for testing  
```

Getting Started

Prerequisites

Python 3.x installed

Install required libraries:
```
pip install -r requirements.txt
```
Usage
Encrypt an image:
```
python encrypt.py input_image.png encrypted_output.enc
```

Decrypt an image:
```
python decrypt.py encrypted_output.enc decrypted_image.png
```
Contributing
Contributions and suggestions are welcome. Please fork the repository and create a pull request.

License
This project is licensed under the MIT License.




