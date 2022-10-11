#pip install pynacl

import base64
from nacl.public import PrivateKey

# =========================================================================== #
# ======================== GENERATION OF PRIVATE KEY ======================== #
# =========================================================================== #

# Method to generate a private key using pynacl
privkey = PrivateKey.generate()
print("Private Key: \n",privkey)

# Method to convert the private key to base64 format
privbkey = (str(privkey))
privbkey_bytes = privbkey.encode("ascii")

privbkey_base64_bytes = base64.b64encode(privbkey_bytes)
privbkey_base64_string = privbkey_base64_bytes.decode("ascii")

# Method to write the .key file
prk = open(r"privatekey.key","w")
prk.write(str(privbkey_base64_string))
prk.close()

# =========================================================================== #

# ========================================================================= #
# ======================= GENERATION OF PUBLIC KEY ======================== #
# ========================================================================= #

# Method to generate a public key using pynacl
pubkey = privkey.public_key
print("Public Key: \n",pubkey)

pubbkey = (str(pubkey))
pubbkey_bytes = pubbkey.encode("ascii")

# Method to convert the public key to base64 format
pubbkey_base64_bytes = base64.b64encode(pubbkey_bytes)
pubbkey_base64_string = pubbkey_base64_bytes.decode("ascii")

# Method to write the .key file
puk = open(r"publickey.key","w")
puk.write(str(pubbkey_base64_string))
puk.close()
# ========================================================================= #
