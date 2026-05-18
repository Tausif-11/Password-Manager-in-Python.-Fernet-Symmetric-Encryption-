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
# Note: To involve a 'master password', you'd usually use a KDF (Key Derivation Function)
# For now, let's just get the basic script running:
key = load_key()
fer = Fernet(key)

pwd = input("WELCOME TO PASSWORD MANAGER. Enter master password: ")
# (In a real app, you'd verify if 'pwd' matches a stored hash here)

def view():
    if not os.path.exists("passwords.txt"):
        print("No passwords saved yet.")
        return
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" not in data: continue
            user, password = data.split("|")
            # We strip the "b'" and "'" from the stored string before decrypting
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