import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import base64
import nacl.utils
from nacl.public import PrivateKey, SealedBox

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        print(self.headers)

        if self.path == '/':
            self.wfile.write(bytes("Home", "utf-8"))

        elif self.path == '/encode':

            head = open(r"head.txt","w+")
            head.write(str(self.headers))
            head.close()
            
            read_head = open('head.txt')
            content = read_head.readlines(0-6)
            cont = content[2]

            final = cont.split(" ",1)
            print(final[1])         

            keys = open(r"keys.txt","w+")
            keys.write(str(final[1]))
            keys.close()
            read_head.close()

            base64_string = final[1]
            base64_bytes = base64_string.encode("ascii")
            
            sample_string_bytes = base64.b64decode(base64_bytes)
            sample_string = sample_string_bytes.decode("ascii")
            print(f"Decoded string: {sample_string}")

            sealed_box = SealedBox(sample_string)

            message = b"Give 10 days Diwali Holiday"

            encrypted = sealed_box.encrypt(message)
            sample_dataset = {
                "results":[
                    {
                        "Encrypted Data": [encrypted]
                    }
                ]
            }

            self.wfile.write(json.dumps({"kind": "HPKE", "JSON": [sample_dataset]}).encode("utf-8"))

        elif self.path == '/decode':
            response = requests.head(self.path)
            print(response.headers["key"])
            self.wfile.write(response.headers["key"])


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
