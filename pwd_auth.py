import hashlib, os

def hash_psd(psd: str) -> str:
    salt = os.urandom(16)
    hashed_psd = hashlib.pbkdf2_hmac('sha256', psd.encode(), salt, 100000)

    return salt.hex() + hashed_psd.hex()

def verify_psd(stored_psd: str, provided_psd: str) -> bool:
    salt = bytes.fromhex(stored_psd[:32])
    stored_hash = stored_psd[32:]
    hashed_psd = hashlib.pbkdf2_hmac('sha256', provided_psd.encode(), salt, 100000)

    return hashed_psd.hex() == stored_hash

if __name__ == "__main__":
    psd_to_score = input("Enter a password to hash: ")
    stored_psd = hash_psd(psd_to_score)
    print(f"Hashed password: {stored_psd}")

    psd_attempt = 'clcoding'
    is_valid = verify_psd(stored_psd, psd_attempt)
    print(f"Password verification result: {is_valid}")