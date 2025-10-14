                                                Image Encryption 
Overview

This project demonstrates simple and effective image encryption using AES (Advanced Encryption Standard) to secure digital images. Users can encrypt and decrypt JPG/PNG files, ensuring privacy for confidential image data. The project includes a Streamlit web app for easy, interactive use.

You can directly encrypt and decrypt images using the interactive web app here:

https://cloudcredits-pbpljgy9cuvxxxnyps7r9q.streamlit.app/

Upload your image, set your AES key, and use the web interface to encrypt or decrypt files instantly.

No installation required – just use the link above!

Features

Encrypt images (.jpg/.png) to protected .enc files

Decrypt encrypted files to restore original images

AES symmetric key encryption for strong security

Command-line scripts and a Streamlit web interface

Folder Structure

```
CLOUDCREDITS/
└── ImageEncryption/
    ├── sample_images/            # Place your test images here
    ├── app.py                   # Streamlit web app
    ├── encrypt.py               # Encrypt images via command line
    ├── decrypt.py               # Decrypt images via command line
    ├── image7.enc               # Example encrypted image
    ├── restored_image7.jpg      # Example decrypted result
    ├── requirements.txt         # List of dependencies
    └── Readme.md                # Project documentation
venv/                            # (Optional) Python virtual environment
.gitignore                       # Files/folders to ignore in git
```

Setup & Installation

Clone the repository

Install dependencies:

pip install -r requirements.txt
(If using a virtual environment, activate it first.)

Usage

Encrypt an Image (Command Line)

```
python encrypt.py sample_images/image.jpg image.enc
```
Encrypts image.jpg and saves as image.enc.

Decrypt an Image (Command Line)

```
python decrypt.py image.enc restored_image.jpg
```
Decrypts image.enc and restores as restored_image.jpg.

Run the Streamlit Web App Locally

```
streamlit run app.py
```
Upload and process images through a simple UI in your browser.

Configuration
Encryption Key:

The AES key is set in the script (default example: pallaviSECURE123). Change it in both encrypt.py and decrypt.py (or in the app) for custom security.

Use exactly the same key for both encryption and decryption.

Requirements
All dependencies are listed in requirements.txt.

streamlit

pillow

pycryptodome

(other packages as listed, if deploying to Streamlit Cloud)

Example Workflow
Encrypt an image: get a .enc file.

Decrypt with the same key: recover the original image exactly.

Use the Streamlit app for a friendly, interactive experience.

License
Open-source for educational purposes – feel free to adapt for your internship or future projects!

Credits
Project by Pallavi for the Cloudcredits Cybersecurity Internship, October 2025.

