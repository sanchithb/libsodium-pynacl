#pip install pynacl

import json
import base64
from nacl.public import SealedBox, PrivateKey

# Open the privatekey.key file and read the key
str_b_private_key = open('privatekey.key', 'r').read()

# Decode the key from base64
b64_b_private_key = base64.urlsafe_b64decode(str_b_private_key)

# Recreate the object from the bytes
private_key = PrivateKey(b64_b_private_key)

# Open the .json file which you got the data from the server
# Rename the file to result.json
# or
# Change the file name in the code below
result_json = 'result.json'

# Loading the JSON file
with open (result_json, 'r') as f:
    response = json.load(f)

# Fetching encrypted message from the JSON file which is in string format
encrypted_data = response["JSON"][0]["results"][0]["Encrypted Data"][0]

# Decode the encrypted message from base64
bytes_encrypted_data = base64.urlsafe_b64decode(encrypted_data)

# Create a SealedBox object using Private Key
unseal_box = SealedBox(private_key)

# Decrypt the message by unsealed_box.decrypt()
bytes_decrypted_data = unseal_box.decrypt(bytes_encrypted_data)


# Decode to JSON format
decrypted_data = json.loads(bytes_decrypted_data.decode('utf-8'))

# Write the decrypted message to a file
with open("decrypted_data.json", "w") as outfile:
    json.dump(decrypted_data, outfile)
