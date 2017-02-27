
import socket
import sys
import argparse
host = 'localhost'
def echo_client(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = (host, port)
	print "Connecting to %s port %s" % server_address
	sock.connect(server_address)
	try:
		# Send data
		message = "Test message. This will be echoed"
		print "Sending %s" % message
		sock.sendall(message)
		# Look for the response
		amount_received = 0
		amount_expected = 10000
		while amount_received < amount_expected:
			data = sock.recv(16)
			if not data:
				break
			amount_received += len(data)
			print "Received: %s" % data
	except socket.errno, e:
		print "Socket error: %s" %str(e)
	except Exception, e:
		print "Other exception: %s" %str(e)
	finally:
		print "Closing connection to the server"
	sock.close()
port=444
echo_client(port)