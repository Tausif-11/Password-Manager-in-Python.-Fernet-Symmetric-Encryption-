# Password-Manager-in-Python.-Fernet-Symmetric-Encryption-
A lightweight Python script to store and secure passwords. Secure your credentials using Fernet symmetric encryption. This Python script generates a local key to encrypt and decrypt account details, keeping your passwords safely stored in a text file.
+--------------------------------+
              |      User Inputs Master PW     |
              +--------------------------------+
                              |
                              v
+------------+       +----------------------------+       +---------------+
|  key.key   | ----> | Loaded by cryptography     | ----> | Active Cipher |
| (Disk File)|       | as Fernet symmetric key    |       |   Instance    |
+------------+       +----------------------------+       +---------------+
|
+--------------------------------------------+
|
v
+----------------------------+
|   Main Interactive Menu    |
+----------------------------+
/                        \
(add) /                          \ (view)
v                            v
+------------------------+   +------------------------+
| Read Account & Pass    |   | Read 'passwords.txt'   |
| Encrypt plain text     |   | Split raw fields (|)   |
| Append to passwords.txt|   | Decrypt ciphertext     |
+------------------------+   | Display to stdout      |
+------------------------+


### Encryption Protocol
The application leverages **Fernet**, an implementation of symmetric authenticated cryptography. Under the hood, Fernet builds upon:
- **AES-128** in CBC mode for encryption.
- **HMAC-SHA256** for authentication/integrity verification.
- An initialization vector (IV) populated via secure random numbers.

---

## Prerequisites

Before running the application, you must install the `cryptography` package:

```bash
pip install cryptography
File Structure
Upon running the script, the following directory environment is maintained:

pm.py (or your chosen script name) — The core execution logic.

key.key — Generated automatically on the first execution. Contains the raw symmetric key. Do not delete or share this file.

passwords.txt — The persistent encrypted file containing data serialized as AccountName|EncryptedCiphertext.

Usage Guide
Initialization / Running:
Launch the application using your terminal environment:

Bash
python pm.py
Master Password Prompt:
Upon startup, you will be prompted to enter a master password.

Note: In this basic implementation version, the master password acts as a gateway placeholder and does not yet derive the cryptographic key dynamically.

Adding a Password (add):

Choose add when prompted.

Enter your account designation (e.g., github).

Enter your plaintext password. The script encrypts this stream instantly and writes it safely to disk.

Viewing Passwords (view):

Choose view when prompted.

The application parses passwords.txt, matches records, and decrypts the cipher strings on-the-fly back into readable credentials.

Exiting (q):

Type q to safely terminate the execution loop.

Core Code Implementation
Python
import os
from cryptography.fernet import Fernet

# 1. Function to generate and save a key if it doesn't exist
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# 2. Check if the key file exists; if not, create it
if not os.path.exists("key.key"):
    write_key()

def load_key():
    return open("key.key", "rb").read()

# 3. Use ONLY the loaded key for Fernet
key = load_key()
fer = Fernet(key)

pwd = input("WELCOME TO PASSWORD MANAGER. Enter master password: ")

def view():
    if not os.path.exists("passwords.txt"):
        print("No passwords saved yet.")
        return
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" not in data: continue
            user, password = data.split("|")
            clean_pass = password.strip("b'").strip("'")
            print(f"Account: {user} | Password: {fer.decrypt(clean_pass.encode()).decode()}")

def add():
    name = input("Account Name: ")
    p_word = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(p_word.encode()).decode() + "\n") 

while True: 
    mode = input("Would you like to add a new password or view existing passwords (view, add, or 'q' to quit)? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:      
        print("Invalid mode.") 
Security Disclaimer & Best Practices
This script is an educational proof-of-concept demonstrating basic symmetric encryption pipelines in Python. For deployment in live production environments, note the following vulnerabilities:

Key Vulnerability: The secret key (key.key) is stored in plaintext on disk. Anyone with filesystem read access can compromise the entire password vault.

Master Password isolation: The master password text input does not currently drive key derivation functions (KDF). To secure this professionally, use a primitive like PBKDF2 or Argon2 to compute the decryption key dynamically out of user memory.
"""

Write out the professional README.md file
with open("README.md", "w", encoding="utf-8") as f:
f.write(readme_content)

print("README.md written successfully.")

Your Markdown file is ready
[file-tag: code-generated-file-0-1779094757819245344]

Here is the complete, professionally formatted `README.md` text designed specifically for your initial code implementation. It covers technical features, workflow architecture, usage instructions, and crucial security disclaimers outlining how your implementation operates.

```markdown
# Minimalist Python Password Manager

A lightweight, local command-line password manager written in Python. This utility stores your credentials locally in an encrypted text file using symmetric encryption via the `cryptography` library.

## Features

- **Local Storage:** All credentials are stored directly on your machine in `passwords.txt`.
- **Symmetric Encryption:** Uses the `cryptography.fernet.Fernet` recipe to ensure passwords cannot be read as plain text.
- **Dynamic Key Generation:** Automatically generates a local encryption key (`key.key`) if one does not already exist.
- **Interactive CLI:** A simple prompt-driven loop to quickly add or retrieve your credentials.

---

## Technical Architecture & Workflow

The application operates on a simple local state model where data storage and encryption keys are isolated on your filesystem:

              +--------------------------------+
              |      User Inputs Master PW     |
              +--------------------------------+
                              |
                              v
+------------+       +----------------------------+       +---------------+
|  key.key   | ----> | Loaded by cryptography     | ----> | Active Cipher |
| (Disk File)|       | as Fernet symmetric key    |       |   Instance    |
+------------+       +----------------------------+       +---------------+
|
+--------------------------------------------+
|
v
+----------------------------+
|   Main Interactive Menu    |
+----------------------------+
/

(add) /                          \ (view)
v                            v
+------------------------+   +------------------------+
| Read Account & Pass    |   | Read 'passwords.txt'   |
| Encrypt plain text     |   | Split raw fields (|)   |
| Append to passwords.txt|   | Decrypt ciphertext     |
+------------------------+   | Display to stdout      |
+------------------------+


### Encryption Protocol
The application leverages **Fernet**, an implementation of symmetric authenticated cryptography. Under the hood, Fernet builds upon:
- **AES-128** in CBC mode for encryption.
- **HMAC-SHA256** for authentication/integrity verification.
- An initialization vector (IV) populated via secure random numbers.

---

## Prerequisites

Before running the application, you must install the `cryptography` package:

```bash
pip install cryptography
File Structure
Upon running the script, the following directory environment is maintained:

pm.py (or your chosen script name) — The core execution logic.

key.key — Generated automatically on the first execution. Contains the raw symmetric key. Do not delete or share this file.

passwords.txt — The persistent encrypted file containing data serialized as AccountName|EncryptedCiphertext.

Usage Guide
Initialization / Running:
Launch the application using your terminal environment:

Bash
python pm.py
Master Password Prompt:
Upon startup, you will be prompted to enter a master password.

Note: In this basic implementation version, the master password acts as a gateway placeholder and does not yet derive the cryptographic key dynamically.

Adding a Password (add):

Choose add when prompted.

Enter your account designation (e.g., github).

Enter your plaintext password. The script encrypts this stream instantly and writes it safely to disk.

Viewing Passwords (view):

Choose view when prompted.

The application parses passwords.txt, matches records, and decrypts the cipher strings on-the-fly back into readable credentials.

Exiting (q):

Type q to safely terminate the execution loop.

Core Code Implementation
Python
import os
from cryptography.fernet import Fernet

# 1. Function to generate and save a key if it doesn't exist
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# 2. Check if the key file exists; if not, create it
if not os.path.exists("key.key"):
    write_key()

def load_key():
    return open("key.key", "rb").read()

# 3. Use ONLY the loaded key for Fernet
key = load_key()
fer = Fernet(key)

pwd = input("WELCOME TO PASSWORD MANAGER. Enter master password: ")

def view():
    if not os.path.exists("passwords.txt"):
        print("No passwords saved yet.")
        return
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" not in data: continue
            user, password = data.split("|")
            clean_pass = password.strip("b'").strip("'")
            print(f"Account: {user} | Password: {fer.decrypt(clean_pass.encode()).decode()}")

def add():
    name = input("Account Name: ")
    p_word = input("Password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(p_word.encode()).decode() + "\n") 

while True: 
    mode = input("Would you like to add a new password or view existing passwords (view, add, or 'q' to quit)? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:      
        print("Invalid mode.") 
Security Disclaimer & Best Practices
This script is an educational proof-of-concept demonstrating basic symmetric encryption pipelines in Python. For deployment in live production environments, note the following vulnerabilities:

Key Vulnerability: The secret key (key.key) is stored in plaintext on disk. Anyone with filesystem read access can compromise the entire password vault.

Master Password isolation: The master password text input does not currently drive key derivation functions (KDF). To secure this professionally, use a primitive like PBKDF2 or Argon2 to compute the decryption key dynamically out of user memory.
