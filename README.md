# 🔐 CryptifyLens &nbsp; ![Python](https://img.shields.io/badge/Made%20with-Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Streamlit](https://img.shields.io/badge/UI-Streamlit-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)

### 🧠 Steganography × Encryption — Hide Secrets in Plain Sight

<p align="center">
  <img src="assets/img1.jpg" width="800" />
</p>

---

## 🚨 Problem Statement

In the digital age, privacy is fragile:
- 🧾 Plain text is easy to intercept  
- 🔐 Encrypted blobs look suspicious  
- 📤 Safe communication is often too technical

> What if your message didn’t *look* like a message at all?

---

## ✅ Solution — CryptifyLens v2

> 🔐 AES Encrypted + 🖼️ LSB Embedded = A normal image hiding powerful secrets.

With CryptifyLens, your secrets vanish inside everyday images — no traces, no hints.

---

## 🧠 How It Works
MESSAGE → 🔐 AES Encryption → 🖼️ Hide in Image → 📤 Share

🖼️ Image → 🔍 Extract + 🔓 Decrypt → 🎯 Secret Revealed


---

## ✨ Features

✅ AES Encryption (Fernet)  
✅ Pixel-Level LSB Steganography  
✅ Secure 44-character Key Generator  
✅ Upload OR Capture Live Image  
✅ Simple Streamlit-Based Interface  
✅ All Data Handled Locally (No Cloud)

---

## 🎯 Real-World Scenario

> Alice posts a scenic image on Instagram.  
> Bob downloads it, uses CryptifyLens, pastes the secret key...  
> 💥 Boom! Secret decoded. No one else even suspects.

---

## 🛠️ Tech Stack

| Tool                 | Purpose                        |
|----------------------|--------------------------------|
| `Python`             | Core logic & scripting         |
| `Streamlit`          | Clean, fast UI                 |
| `OpenCV`             | Live camera support            |
| `Pillow`             | Image processing               |
| `Cryptography`       | AES encryption via Fernet      |
| `NumPy`              | Image data manipulation        |

---

## 🚀 Getting Started

Clone and run locally:

```bash
# 1. Clone this repo
git clone https://github.com/mekhushi/CryptifyLens.git
cd CryptifyLens

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py
```
---

## ⚠️ Disclaimer
This tool is for educational and ethical use only.
❌ Do not use CryptifyLens for malicious or illegal purposes.

---

## 🤝 Contributions
Want to contribute or suggest features?
Feel free to fork the repo, raise issues, or submit pull requests!

---
## 👨‍💻 Author
Made with ❤️ by @mekhushi

---
⚠️ Note: Due to Streamlit Cloud's camera/input limitations and OpenCV dependencies, deployment may face issues. The project runs fully offline.




