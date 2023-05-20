import jwt

# Encoding & Decoding Tokens with HS256
key = "secret"
encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
# print(encoded_jwt)
decoded_jwt = jwt.decode(encoded_jwt, key, algorithms=["HS256"])
# print(decoded_jwt)

# Encoding & Decoding Tokens with RS256 (RSA)
private_key = b"-----BEGIN PRIVATE KEY-----\nMIGEAgEAMBAGByqGSM49AgEGBS..."
public_key = b"-----BEGIN PUBLIC KEY-----\nMHYwEAYHKoZIzj0CAQYFK4EEAC..."
rsa_encoded = jwt.encode({"some : payload"}, private_key, algorithm="RS256")
print(rsa_encoded)
rsa_decoded = jwt.decode(rsa_encoded, public_key, algorithms=["RS256"])
print(rsa_decoded)