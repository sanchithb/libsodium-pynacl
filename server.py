# pip install pynacl

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import base64
from nacl.public import SealedBox
import pickle

# Server Initiation

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):

# GET Request Handler

    def do_GET(self):

        # Send response status code 200 (OK)
        self.send_response(200)

        # Send headers, We are sending the json data
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # url path
        if self.path == '/':
            
            self.wfile.write(bytes("Home", "utf-8"))

        elif self.path == '/encode':

            # Initialize a file where headers are dumped

            head = open(r"head.txt","w+")
            head.write(str(self.headers))
            head.close()
            
            # Read the headers from the file and extract the key

            read_head = open('head.txt')
            content = read_head.readlines(0-6)
            cont = content[2]

            final = cont.split(" ",1)
            print(final[1])         

            keys = open(r"keys.txt","w+")
            keys.write(str(final[1]))
            keys.close()
            read_head.close()

            # Assign a variable to the key

            str_p_public_key = final[1]

            # Decode it from base64

            b64_p_public_key = base64.b64decode(str_p_public_key)

            # Unpickle it

            public_key = pickle.loads(b64_p_public_key)

            # Create a SealedBox object

            sealed_box = SealedBox(public_key)

            message = b"Give 10 days Diwali Holiday"

            encrypted = sealed_box.encrypt(message)

            # encrypted is of type bytes and it is not JSON Serializable
            # We convert it to string and send it

            b64_encrypted = base64.b64encode(encrypted)

            str_encrypted = b64_encrypted.decode("utf-8")

            sample_dataset = {
                "results":[
                    {
                        "Encrypted Data": [str_encrypted]
                    }
                ]
            }

            self.wfile.write(json.dumps({"kind": "HPKE", "JSON": [sample_dataset]}).encode("utf-8"))


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
