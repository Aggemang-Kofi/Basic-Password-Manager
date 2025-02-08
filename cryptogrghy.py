from cryptography.fernet import Fernet

# Generate & store the key securely (Do this once)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load encryption key
def load_key():
    return open("key.key", "rb").read()

# Encrypt password
def encrypt_password(password, key):
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

# Decrypt password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    return f.decrypt(encrypted_password.encode()).decode()

# Run this once to generate a key
generate_key()
