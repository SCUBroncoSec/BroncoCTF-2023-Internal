import socketserver
import time
import threading
import random
import os



class Service(socketserver.BaseRequestHandler):
	def handle(self):
		print("New Connection")

		offset = random.randint(10, 20)
		start_time = int(time.time())

		script_dir = os.path.dirname(__file__)
		rel_path = "empire_striketh_back.txt"
		abs_file_path = os.path.join(script_dir, rel_path)

		with open(abs_file_path, 'rb') as script:
			while(True):
				if(int(time.time()) != start_time + offset):
					data = script.read(1)
					self.send(data, newline = False)
				else:
					flag = "broncoctf{Alas_n@ughty_dr0id!}"
					
					self.send(flag.encode('utf-8'), newline=False)

					start_time = int(time.time())
					offset = random.randint(10, 20)
				
				if data == None:
					script.seek(0)
	
	def send(self, string, newline=True):
		if newline:
			string = string + '\n'
		self.request.sendall(string)
		time.sleep(0.01)
	
	def recieve(self, prompt = " > "):
		self.send(prompt, newline=False)
		return self.request.recv(4096).strip()

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
