import streamlit as st
from camera_input_live import camera_input_live
from PIL import Image
import numpy as np
import io
import cv2
from crypto_utils import generate_key, encrypt_message, decrypt_message
from stego_utils import encode_message, decode_message

st.set_page_config(page_title="CryptifyLens ", layout="centered")
st.title("🔐 CryptifyLens")
st.markdown("Encrypt, hide, and retrieve secret messages inside images using steganography + AES encryption.")

tabs = st.tabs(["📥 Encrypt & Embed", "🔓 Decrypt & Extract"])

with tabs[0]:
    st.subheader("📸 Step 1: Capture Image")
    img_data = camera_input_live()

    if img_data:
        pil_image = Image.open(io.BytesIO(img_data.getvalue())).convert("RGB")
        image = np.array(pil_image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        st.image(image, caption="Captured Image", use_container_width=True)

        st.subheader("✍️ Step 2: Enter Message")
        msg = st.text_input("Your secret message:")

        if msg:
            if st.button("🔐 Encrypt & Embed"):
                key = generate_key()
                encrypted = encrypt_message(msg, key)
                encoded_img = encode_message(image, encrypted)

                st.success("✅ Message encrypted & embedded successfully!")
                st.image(encoded_img, caption="Stego Image",use_container_width=True)
                cv2.imwrite("stego_image.png", encoded_img)

                st.code(f"🔑 Your Secret Key:\n{key.decode()}")
                with open("stego_image.png", "rb") as file:
                    st.download_button("📥 Download Stego Image", file, "stego_image.png", "image/png")
        else:
            st.info("👆 Enter a secret message.")

with tabs[1]:
    st.subheader("📤 Upload Stego Image")
    uploaded = st.file_uploader("Upload the image containing the hidden message", type=["png", "jpg", "jpeg"])
    key_input = st.text_input("🔑 Enter the secret key you received:").strip()

    if uploaded and key_input:
        img = Image.open(uploaded).convert("RGB")
        image = np.array(img)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if len(key_input) != 44:
            st.error("🚫 Invalid Fernet key! It must be exactly 44 characters (base64-encoded).")
        else:
            try:
                extracted_bytes = decode_message(image)
                decrypted = decrypt_message(extracted_bytes, key_input.encode())
                st.success("✅ Message extracted & decrypted successfully:")
                st.code(decrypted)
            except Exception as e:
                st.error(f"❌ Decryption failed. Reason: {str(e)}")
    elif uploaded and not key_input:
        st.info("✍️ Please enter the secret key you received.")
