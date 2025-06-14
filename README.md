# 🔐 CryptifyLens v2 — Hide & Protect Messages Inside Images

> **Steganography meets Encryption.** A secure web app to encrypt text using AES and hide it inside images using LSB steganography. All powered by Python + Streamlit.

---

## 📌 Problem Statement

In a world full of screenshots, leaks, and prying eyes 👀 — sharing secret messages safely is harder than it should be.

![Stego Output](assets/img1.jpg)

Most people rely on:
- Plain text apps 🧾 (easy to intercept)
- Encrypted messages 📩 (still visible as “encrypted blobs”)

But what if… your secret message **wasn’t even visible**?

---

## 💡 Solution

**CryptifyLens v2** lets you:
1. 📸 Capture or upload an image
2. 🔐 Encrypt your message using AES (Fernet)
3. 🖼️ Hide it inside the image using LSB steganography
4. 📤 Share the image — looks normal, but carries secrets

Even if someone opens the image... they’ll see **nothing.**  
Unless they have the **key** — and this app.

---

## 🧠 Features

- 🔐 AES-based text encryption (Fernet)
- 🖼️ LSB steganography for image-based hiding
- 📸 Capture image live from camera
- 🧠 Secret key generator (44-char Fernet key)
- 📤 Upload + extract + decrypt interface
- 💻 Fully built with Streamlit

---

## 🎥 Demo Preview

<p align="center">
  <img src="demo.gif" width="500px" />
</p>

> _Looks like an image. Acts like a vault._

---

## 🛠️ Tech Stack

- **Python** – Core logic
- **Streamlit** – UI & deployment
- **OpenCV** – Image handling
- **Fernet (Cryptography)** – AES-based encryption
- **NumPy** – Array manipulation
- **Pillow** – Image conversion

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/mekhushi/CryptifyLens-v2.git
cd CryptifyLens-v2

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
