import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

def derive_key(password: str, salt: bytes = None) -> bytes:
    if salt is None:
        salt = os.urandom(16)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=390000)
    key = kdf.derive(password.encode())
    return salt, base64.urlsafe_b64encode(key)

def encrypt_file(file_path: str, password: str):
    try:
        with open(file_path, "rb") as file:
            data = file.read()
        salt, key = derive_key(password)
        f = Fernet(key)
        encrypted_data = f.encrypt(data)
        encrypted_file_path = file_path + ".enc"
        with open(encrypted_file_path, "wb") as encrypted_file:
            encrypted_file.write(salt + encrypted_data)
        messagebox.showinfo("Encryption Successful", f"File encrypted and saved as: {encrypted_file_path}")
    except Exception as e:
        messagebox.showerror("Encryption Error", str(e))

def decrypt_file(file_path: str, password: str):
    try:
        with open(file_path, "rb") as encrypted_file:
            combined_data = encrypted_file.read()
            salt = combined_data[:16]
            encrypted_data = combined_data[16:]
        _, key = derive_key(password, salt)
        f = Fernet(key)
        decrypted_data = f.decrypt(encrypted_data)
        decrypted_file_path = file_path[:-4]
        with open(decrypted_file_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)
        messagebox.showinfo("Decryption Successful", f"File decrypted and saved as: {decrypted_file_path}")
    except Exception as e:
        messagebox.showerror("Decryption Error", str(e))

def browse_file(entry_widget):
    file_path = filedialog.askopenfilename()
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, file_path)

def main():
    window = tk.Tk()
    window.title("Advanced Encryption Tool")
    file_label = tk.Label(window, text="Select File:")
    file_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    file_entry = tk.Entry(window, width=50)
    file_entry.grid(row=0, column=1, padx=5, pady=5)
    browse_button = tk.Button(window, text="Browse", command=lambda: browse_file(file_entry))
    browse_button.grid(row=0, column=2, padx=5, pady=5)
    password_label = tk.Label(window, text="Enter Password:")
    password_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    password_entry = tk.Entry(window, show="*", width=50)
    password_entry.grid(row=1, column=1, padx=5, pady=5)
    encrypt_button = tk.Button(window, text="Encrypt", command=lambda: encrypt_file(file_entry.get(), password_entry.get()))
    encrypt_button.grid(row=2, column=0, columnspan=3, padx=5, pady=10)
    decrypt_button = tk.Button(window, text="Decrypt", command=lambda: decrypt_file(file_entry.get(), password_entry.get()))
    decrypt_button.grid(row=3, column=0, columnspan=3, padx=5, pady=10)
    window.mainloop()

if __name__ == "__main__":
    main()