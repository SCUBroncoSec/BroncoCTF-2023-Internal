##############################
##############################
# ***   bes.py     ***
# Bronco Encryption Server
# Built using AES!
##############################
##############################

import socketserver
import time
import threading
from Crypto.Cipher import AES
from binascii import hexlify, unhexlify
from flag import flag

#Check if a string is hex
def is_hex(s):
	try:
		int(s, 16)
		return True
	except ValueError:
		return False

#Pad message with 0s
def pad_plaintext(pt):
    pad = 32 - (len(pt) % 32)
    ct = pt + ("0" * pad)
    return ct

#Encrypts a given message
def aesEncrypt(msg):
	aesKey = aesIV = flag
	
	aes = AES.new(unhexlify(aesKey), AES.MODE_CBC, unhexlify(aesIV)) #create aes cipher in cbc mode

	if(len(msg) % 32 != 0): #pad message if needed
		msg = pad_plaintext(msg)

	pt= unhexlify(msg)
	ct = aes.encrypt(pt) #encrypt plaintext using aes
	response = hexlify(ct).decode()
	return response

#Decrypts a given message
def aesDecrypt(msg):
	aesKey = flag
	aesIV = flag
	aes = AES.new(unhexlify(aesKey), AES.MODE_CBC, unhexlify(aesIV)) #create aes cipher in cbc mode

	ct= unhexlify(msg)
	pt = aes.decrypt(ct) #decrypt ciphertext using aes
	response = hexlify(pt).decode()
	return response

class Service(socketserver.BaseRequestHandler):
	def handle(self):
		print("New Connection")

		self.send("Welcome to the Bronco Encryption Server")
		self.send("Select an option to continue:\n1) Encrypt Message\n2) Decrypt Message")

		option = int(self.recieve())
		while(option != 1 and option != 2):
			self.send("Whoops, that is not a valid choice. Please try again.")
			option = int(self.recieve())

		if option == 1:
			self.send("Please enter a hexadecimal message to encrypt.")
			pt = self.recieve()

			while(not is_hex(pt)):
				self.send('Message must be a hexadecimal string. Please try again')
				ct = self.recieve()

			ct = aesEncrypt(pt)

			self.send("Here is your encrypted message:")
			self.send(ct)

		elif option == 2:
			self.send("Please enter a hexadecimal message to decrypt.")
			ct = self.recieve()

			while(len(ct) % 32 != 0 or not is_hex(ct)):
				self.send('Ciphertext must be a multiple of 32 hexadecimal characters. Please try again')
				ct = self.recieve()

			pt = aesDecrypt(ct)

			self.send("Here is your decrypted message:")
			self.send(pt)
			

	def send(self, string, newline=True):
		if newline:
			string = string + '\n'
		self.request.sendall(string.encode())
	
	def recieve(self, prompt = " > "):
		self.send(prompt, newline=False)
		return self.request.recv(4096).strip().decode()

class ThreadedService(socketserver.ThreadingMixIn, socketserver.TCPServer, socketserver.DatagramRequestHandler):
	pass

def main():

    port = 8080
    host = '0.0.0.0'

    service = Service
    server = ThreadedService((host, port), service)

    server.allow_reuse_address = True

    server_thread = threading.Thread(target=server.serve_forever)

    server_thread.daemon = True
    server_thread.start()

    print(f"Server started on port {port}")

    while(True):
        time.sleep(60)

if(__name__ == "__main__"):
    main()
