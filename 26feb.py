from cryptography.fernet import Fernet # type: ignore

key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

print("key created.")
import os
from cryptography.fernet import Fernet
from datetime import datetime

def load_key():
    return open("secret.key", "rb").read()

key = load_key()
fernet = Fernet(key)

def add_entry():
    content = input("\nwrite your diary entry: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {content}\n"
    encrypted_entry = fernet.encrypt(entry.encode())
    with open("diary.enc", "ab") as diary_file:
        diary_file.write(encrypted_entry + b"\n")
    print("entry saved.")

def view_entries():
    if not os.path.exists("diary.enc"):
        print("no entries found.")
        return
    print("\n--- decryped diary ---")
    with open("diary.enc", "rb") as diary_file:
        for line in diary_file:
            if line.strip():
                decrypted = fernet.decrypt(line).decode()
                print(decrypted)

while True:
    choice = input("\n[1] write  [2] view  [3] exit: ")
    if choice == '1':
        add_entry()
    elif choice == '2':
        view_entries()
    elif choice == '3':
        break