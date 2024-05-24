import base64
from cryptography.fernet import Fernet
import hashlib

def generate_key(passcode: str) -> bytes:
    hasher = hashlib.sha256()
    hasher.update(passcode.encode())
    return base64.urlsafe_b64encode(hasher.digest())

def encrypt_file(file_path: str, passcode: str):
    key = generate_key(passcode)
    cipher = Fernet(key)
    
    with open(file_path, 'rb') as file:
        file_data = file.read()
    
    encrypted_data = cipher.encrypt(file_data)
    
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)
    
    print(f"File {file_path} has been encrypted.")

def decrypt_file(file_path: str, passcode: str):
    key = generate_key(passcode)
    cipher = Fernet(key)
    
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    
    try:
        decrypted_data = cipher.decrypt(encrypted_data)
    except cryptography.fernet.InvalidToken:
        print("Invalid passcode. Unable to decrypt the file.")
        return
    
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)
    
    print(f"File {file_path} has been decrypted.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Locker App to encrypt/decrypt files using a passcode.")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode to run the locker app in.")
    parser.add_argument("file", help="File to be encrypted or decrypted.")
    parser.add_argument("passcode", help="Passcode for encryption/decryption.")

    args = parser.parse_args()

    if args.mode == "encrypt":
        encrypt_file(args.file, args.passcode)
    elif args.mode == "decrypt":
        decrypt_file(args.file, args.passcode)
