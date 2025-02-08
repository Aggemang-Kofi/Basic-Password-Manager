# Basic Password Manager

## Overview
A simple password manager that uses the `cryptography` library to securely store and manage passwords. It allows for password encryption, decryption, and safe key storage.

## Features
- **Encryption**: Encrypt and decrypt passwords using a strong key.
- **Key Management**: Generate and store encryption keys securely.
- **Secure Storage**: The encrypted passwords are stored safely and can be decrypted only with the correct key.

## Setup

### Prerequisites
To run this project, you need to have the following:
- Python 3.x installed
- `cryptography` library installed. You can install it using pip:
    ```bash
    pip install cryptography
    ```

### Generating the Key
Run the script once to generate the encryption key:
```bash
python3 main.py
