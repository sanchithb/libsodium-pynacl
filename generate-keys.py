#pip install pynacl

import base64
from nacl.public import PrivateKey
import pickle

# =========================================================================== #
# ======================== GENERATION OF PRIVATE KEY ======================== #
# =========================================================================== #

# Method to generate a private key using pynacl
private_key = PrivateKey.generate()
print("Private Key: \n",private_key)

# Pickle the private key

p_private_key = pickle.dumps(private_key)

# Encode the private key to base64

b64_p_private_key = base64.b64encode(p_private_key)

# Convert the encoded private key to string to send over http
# allthough this method is skipable for private key as we are not transferring

str_p_private_key = b64_p_private_key.decode("utf-8")

# Method to write the .key file
prk = open(r"privatekey.key","w")
prk.write(str_p_private_key)
prk.close()

# =========================================================================== #

# ========================================================================= #
# ======================= GENERATION OF PUBLIC KEY ======================== #
# ========================================================================= #

# Method to generate a public key using pynacl
public_key = private_key.public_key
print("Public Key: \n",public_key)

# Pickle the public key

p_public_key = pickle.dumps(public_key)

# Encode the public key to base64

b64_p_public_key = base64.b64encode(p_public_key)

# Convert the encoded public key to string to send over http

str_p_public_key = b64_p_public_key.decode("utf-8")

# Method to write the .key file
puk = open(r"publickey.key","w")
puk.write(str_p_public_key)
puk.close()

# ========================================================================= #
