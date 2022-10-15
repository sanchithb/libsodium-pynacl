#pip install pynacl

import json
import base64
from nacl.public import SealedBox
import pickle

# Open the privatekey.key file and read the key
str_p_private_key = open('privatekey.key', 'r').read()

# Decode the key from base64
b64_p_private_key = base64.b64decode(str_p_private_key)

# Unpickle the key
private_key = pickle.loads(b64_p_private_key)

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
bytes_encrypted_data = base64.b64decode(encrypted_data)

# Create a SealedBox object using Private Key
unseal_box = SealedBox(private_key)

# Decrypt the message by unsealed_box.decrypt()
decrypted_data = unseal_box.decrypt(bytes_encrypted_data)

# Print the decrypted message
print(decrypted_data)

# Write the decrypted message to a file
msg = open(r"Decrypted Data.txt","w")
msg.write(str(decrypted_data))
msg.close()
