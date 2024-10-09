from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os


class CryptoService:
    def __init__(self, secret_key: str):
        self.salt = os.urandom(16)
        self.secret_key = self.derive_key(secret_key)

    def derive_key(self, secret_key: str) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=default_backend(),
        )
        return kdf.derive(secret_key.encode())

    def encrypt(self, plaintext: str) -> str:
        iv = os.urandom(16)
        cipher = Cipher(
            algorithms.AES(self.secret_key), modes.CFB(iv), backend=default_backend()
        )
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
        return urlsafe_b64encode(iv + ciphertext).decode()

    def decrypt(self, ciphertext: str) -> str:
        decoded_data = urlsafe_b64decode(ciphertext.encode())
        iv = decoded_data[:16]
        ciphertext = decoded_data[16:]
        cipher = Cipher(
            algorithms.AES(self.secret_key), modes.CFB(iv), backend=default_backend()
        )
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        return plaintext.decode()
