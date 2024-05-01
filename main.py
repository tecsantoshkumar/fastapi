from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
import binascii
import base64

app = FastAPI()

class EncryptRequest(BaseModel):
    password: str
    salt: str
    plain_text: str

class EncryptResponse(BaseModel):
    encrypted_hex: str
    encrypted_base64: str

@app.post("/encrypt/", response_model=EncryptResponse)
def encrypt_string(req: EncryptRequest):
    key = PBKDF2(req.password, req.salt.encode(), dkLen=32, count=65536)
    iv = b'\x00' * AES.block_size
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(req.plain_text.encode(), AES.block_size))
    encrypted_hex = binascii.hexlify(ciphertext).decode()
    encrypted_base64 = base64.b64encode(ciphertext).decode()
    return {"encrypted_hex": encrypted_hex, "encrypted_base64": encrypted_base64}

class DecryptRequest(BaseModel):
    password: str
    salt: str
    encrypted_text: str

@app.post("/decrypt/")
def decrypt_string(req: DecryptRequest):
    try:
        key = PBKDF2(req.password, req.salt.encode(), dkLen=32, count=65536)
        encrypted_ciphertext = base64.b64decode(req.encrypted_text)
        iv = b'\x00' * AES.block_size
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(encrypted_ciphertext), AES.block_size)
        return plaintext.decode()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
