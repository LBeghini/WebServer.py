from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

while True:
	print('Ready to serve...')
	print(f'Listen at: {serverSocket.getsockname()}')
	connectionSocket, addr = serverSocket.accept()
	print("Connected\n\n")

	try:
		message = connectionSocket.recv(1024)
		print(f"{message.decode()}", sep='\n')
		print(message)
		if len(message.split()) != 0:
			filename = message.split()[1]
			print(message)
			print(f"Requested file: {message.split()[1][1:]}")
			f = open(filename[1:])
			outputdata = f.read()
			connectionSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n", 'utf8'))
			print(f"Sending response...")
			for i in outputdata:
				connectionSocket.send(bytes(i, 'utf8'))
			connectionSocket.send(bytes("\r\n", 'utf8'))
			print("Closing connection...\n\n")
			connectionSocket.close()
		else:
			raise IOError

	except IOError:
		print("Not found.\nSending response...")
		connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n", 'utf8'))
		connectionSocket.send(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n", 'utf8'))
		print("Closing connection...\n\n")
		connectionSocket.close()
