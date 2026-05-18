# 🔐 Password Manager (Python - Fernet Encryption)

A lightweight command-line password manager built using Python.  
It securely stores credentials locally using symmetric encryption via the `cryptography` library (Fernet).

---

## 🚀 Features

- 🔒 AES-based symmetric encryption (Fernet)
- 📁 Local storage of encrypted passwords
- 🧠 Automatic key generation (`key.key`)
- 💻 Simple command-line interface (CLI)
- ➕ Add and view stored credentials
- ⚡ Lightweight and beginner-friendly

---

## 🏗️ How It Works


User Input (Master Password)
↓
Load / Generate key.key
↓
Create Fernet Cipher Instance
↓
CLI Menu
/
ADD VIEW
| |
Encrypt Decrypt
| |
Store in Read from
passwords.txt passwords.txt


---

## 🔐 Encryption Details

This project uses **Fernet symmetric encryption**, which includes:

- AES-128 (CBC mode)
- HMAC-SHA256 (data integrity)
- Secure random IV generation

---

## 📦 Installation

Install required dependency:

```bash
pip install cryptography
📁 File Structure
Password Manager Project/
│
├── password_Manager.py   # Main program
├── key.key               # Encryption key (auto-generated)
├── passwords.txt         # Encrypted password storage
├── .gitignore            # Ignored sensitive files
└── README.md             # Documentation
▶️ Usage

Run the program:

python password_Manager.py
🧭 Menu Options
➕ Add Password
Enter account name
Enter password
Stored in encrypted format
👁️ View Passwords
Decrypts and displays stored credentials
❌ Exit
Type q to quit safely
⚠️ Security Warning

This project is for educational purposes only.

Limitations:
❌ Encryption key stored locally (key.key)
❌ No password-based key derivation (no PBKDF2/Argon2)
❌ Not suitable for production use
Improvements for production:
Use KDF (PBKDF2 / Argon2)
Store key in secure vault / OS keychain
Use database instead of plain text file
💡 Future Improvements
GUI version (Tkinter / PyQt)
Encrypted database storage
Master password authentication system
Clipboard auto-clear feature
📜 License

MIT License
