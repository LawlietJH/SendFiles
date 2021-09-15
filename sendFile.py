
import atexit
import base64
import socket
import json
import time
import sys
import os

class Server:
	
	def __init__(self):
		
		self.HOSTNAME = socket.gethostname()
		self.LHOST = socket.gethostbyname(self.HOSTNAME)
		self.PORT = 57575
		
		self.downloadPath = 'received\\'
	
	def progressBar(self, pos, chunks, qty=30, c=('█',' '), bfc=2**16): # bfc = bytes for chunk
		
		block = 100 / qty
		chunk = 100 / chunks
		
		percent  = chunk * pos
		progress = percent // block
		progress += 1 if percent % block > 0 else 0
		spaces   = qty - progress
		# ~ if pos == chunks: percent = 100
		bar = '{}% |{}{}|'.format(str(int(percent)).rjust(3),c[0]*int(progress), c[1]*int(spaces))
		
		return bar
	
	def receive(self):
		
		print(f'\n IP: {server.LHOST}')
		
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server.bind((self.LHOST, self.PORT))
		self.server.listen(1)
		
		print('\n En escucha...')
		
		self.client, self.clientIP = self.server.accept()
		
		RHOSTNAME = self.client.recv(64).decode()
		
		if RHOSTNAME:
			
			self.client.send('ok'.encode())
			
			resp = self.client.recv(1024).decode()
			info = json.loads(resp)
			
			print('\n\n File: {}\n Size: {} bytes\n'.format(info['fileName'], info['fileSize']))
			
			if not os.path.exists(self.downloadPath):
				os.mkdir(self.downloadPath)
			
			if os.path.exists(self.downloadPath+info['fileName']):
				print('\n\n Ya fue descargado')
				self.client.send('ko'.encode())
			else:
				self.client.send('ok'.encode())
				with open(self.downloadPath+info['fileName'], 'wb') as f:
					for i in range(info['chunksLen']):
						bar = self.progressBar(i+1, info['chunksLen'], bfc=info['chunkSize'])
						print('\r [+] Downloading: '+bar, end='')
						chunk = self.client.recv(info['chunkSize'])
						f.write(base64.b64decode(chunk))
						self.client.send('ok'.encode())
				print('\n\n Archivo Recibido!\n')
		
		self.server.close()

class Client:
	
	def __init__(self):
		
		self.HOSTNAME = socket.gethostname()
		self.LHOST = socket.gethostbyname(self.HOSTNAME)
		self.PORT = 57575
	
	def getChunks(self, data, bfc=2**16):	# 2^16 = 65536 bytes = 64 kb, bfc = bytes for chunk
		parts = (len(data) // bfc)
		parts += 1 if (len(data) % bfc) else 0
		chunks = [ data[bfc*i:bfc*(i+1)] for i in range(parts) ]
		return chunks
	
	def send(self, RHOST, fileName):
		
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client.connect((RHOST, self.PORT))
		
		self.client.send(self.HOSTNAME.encode())
		
		resp = self.client.recv(2).decode()
		
		if resp == 'ok':
			
			print('\n Enviando...')
			
			with open(fileName, 'rb') as f:
				chunkSize = 2**10
				data = base64.b64encode(f.read())
				chunks = self.getChunks(data, bfc=chunkSize)
				info = {
					'fileName': fileName,
					'fileSize': os.path.getsize(fileName),
					'chunksLen': len(chunks),
					'chunkSize': chunkSize
				}
				info = json.dumps(info, indent=4)
				self.client.send(info.encode())
				
				if self.client.recv(2).decode() == 'ok':
					time.sleep(1)
					for chunk in chunks:
						self.client.send(chunk)
						self.client.recv(2)
				else:
					print('ko :c')
		else:
			print('conexion rechazada')
		
		self.client.close()



@atexit.register
def close():
	if server:
		if not server.server._closed:
			server.server.close()
		
	if client:
		if not client.client._closed:
			client.client.close()
	
	time.sleep(25)



if __name__ == '__main__':
	
	# Servidor -----------------------------------
	client = None
	server = Server()
	server.receive()
	
	# Cliente ------------------------------------
	# ~ fileName = 'file_name.ext'
	# ~ server = None
	# ~ client = Client()
	# ~ client.send('127.0.0.1', fileName)
	





