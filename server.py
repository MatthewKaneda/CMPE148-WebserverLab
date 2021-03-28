# import socket module

from socket import *

import sys
import os
import time

try:
	# AF_INET for IPv4 protocols
	# SOCK_STREAM for TCP
	serverSocket = socket(AF_INET, SOCK_STREAM)
	serverPort = 80

	# serverSocket.close()
	# sys.exit()

	# Prepare a server socket

	# Binds socket to server address and server port
	serverSocket.bind(('', serverPort))
	# only listen to 1 connection
	serverSocket.listen(1)

	print(f"Web server open on port: {serverPort}")

	while True:
		# Establish connection

		print('Ready to serve... \n')

		connectionSocket, addr = serverSocket.accept()

		try:
			# try receiving request message
			message = connectionSocket.recv(1024)
			print(f"Request message: {message}\n")

			filename = message.split()[1]

			print(f"filename: {filename}\n")

			f = open(filename[1:])

			outputData = f.read()
			print(f"OutputData: {outputData}\n")

			# Send the content of the requested file to the client

			for i in outputData:
			# for i in range(0, len(outputData)):
				# print(i)
				# print(outputData[i])
				connectionSocket.send(i.encode())
				# connectionSocket.send(outputData[i].encode())

			connectionSocket.send("\r\n".encode())

			# Send one HTTP header line into socket
			connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())

			connectionSocket.close()

		except IOError:
			# Send response message for file not found
			# connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())
			connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())

			# Close client socket
			connectionSocket.close()

	serverSocket.close()
	sys.exit()

except KeyboardInterrupt:
	print("Keyboard Interrupt... \nAttempting to close socket\n")
	serverSocket.close()
	time.sleep(5)
	print("Server Socket close command issued\n")
	try:
		sys.exit(0)
	except SystemExit:
		os._exit(0)
