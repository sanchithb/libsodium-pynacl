#pip install pynacl

import base64
from nacl.public import PrivateKey

# =========================================================================== #
# ======================== GENERATION OF PRIVATE KEY ======================== #
# =========================================================================== #

# Method to generate a private key using pynacl
private_key = PrivateKey.generate()
print("Private Key: \n",private_key)

# Extract the bytes from the private key object

b_private_key = PrivateKey.__bytes__(private_key)

# Encode the private key to base64

b64_b_private_key = base64.urlsafe_b64encode(b_private_key)

# Convert the encoded private key to string to send over http
# allthough this method is skipable for private key as we are not transferring

str_b_private_key = b64_b_private_key.decode("utf-8")

# Method to write the .key file
prk = open(r"privatekey.key","w")
prk.write(str_b_private_key)
prk.close()

# =========================================================================== #

# ========================================================================= #
# ======================= GENERATION OF PUBLIC KEY ======================== #
# ========================================================================= #

# Method to generate a public key using pynacl
public_key = private_key.public_key
print("Public Key: \n",public_key)

# Extract the bytes from the private key object

b_public_key = private_key.public_key.__bytes__()

# Encode the public key to base64

b64_b_public_key = base64.b64encode(b_public_key)

# Convert the encoded public key to string to send over http

str_b_public_key = b64_b_public_key.decode("utf-8")

# Method to write the .key file
puk = open(r"publickey.key","w")
puk.write(str_b_public_key)
puk.close()

# ========================================================================= #
