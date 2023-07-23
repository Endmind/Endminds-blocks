import base64

def encode_pwd(plaintext_pwd: str):
    return base64.b64encode(plaintext_pwd.encode('utf-8'))

def decode_pwd(encoded_pwd):
    return base64.b64decode(encoded_pwd).decode('utf-8')

print(encode_pwd('1234'))
print(decode_pwd(b'MTIzNA=='))

