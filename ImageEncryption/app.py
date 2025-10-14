import streamlit as st
from PIL import Image
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import io

def encrypt_image(image, key):
    # Save original image mode and size for decryption
    img_bytes = image.tobytes()
    mode = image.mode
    size = image.size

    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(img_bytes, AES.block_size))
    # Add mode, size, iv to header for reconstruction
    header = mode.encode().ljust(10, b' ')   # 10 bytes for mode
    width = size[0].to_bytes(4, byteorder='big')
    height = size[1].to_bytes(4, byteorder='big')

    return header + width + height + iv + encrypted

def decrypt_image(data, key):
    mode = data[0:10].decode().strip()           # 0:10 mode
    width = int.from_bytes(data[10:14], 'big')   # 10:14 width
    height = int.from_bytes(data[14:18], 'big')  # 14:18 height
    iv = data[18:34]                             # 18:34 iv
    encrypted = data[34:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    img_bytes = unpad(cipher.decrypt(encrypted), AES.block_size)
    return Image.frombytes(mode, (width, height), img_bytes)

st.title("Image Encryption App (AES)")

key_input = st.text_input("Enter a 16-character AES key:", value="pallaviSECURE123")
key = key_input.encode().ljust(16, b'0')[:16]  # Ensure 16 bytes

action = st.radio("Action", ["Encrypt", "Decrypt"])
uploaded_file = st.file_uploader("Upload Image/File", type=["jpg", "jpeg", "png", "enc"])

if uploaded_file and action == "Encrypt":
    image = Image.open(uploaded_file)
    encrypted_data = encrypt_image(image, key)
    st.download_button("Download Encrypted File", encrypted_data, file_name="encrypted.enc")
    st.success("Image encrypted! Download your .enc file above.")

elif uploaded_file and action == "Decrypt":
    encrypted_data = uploaded_file.read()
    try:
        image = decrypt_image(encrypted_data, key)
        buf = io.BytesIO()
        image.save(buf, format="PNG")
        st.image(image, caption="Decrypted Image")
        st.download_button("Download Decrypted Image", buf.getvalue(), file_name="decrypted.png")
        st.success("Image decrypted! View and download above.")
    except Exception as e:
        st.error(f"Decryption failed: {e}")
