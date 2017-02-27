import socket
host_name = socket.gethostname()
def get_hostname():
	host_name = socket.gethostname()
	print "Host name: %s" %host_name
def get_hostbyname():
	host_name = socket.gethostname()
	host_name = "www.baidu.com"
	address = socket.gethostbyname(host_name)
	print "IP address: %s" %address
def get_hostnamebyip(address):
	address="66.249.71.15"
	host_name=socket.gethostbyaddr(address)
	print "Host name :%s" %host_name[0]

def get_remote_machine_info():
	remote_host = 'www.python.org'
	try:
		print "Url:",remote_host,
		print "IP address: %s" %socket.gethostbyname(remote_host)
	except socket.error, err_msg:
		print "%s: %s" %(remote_host, err_msg)
	
def find_service_name():
	protocolname1 = 'tcp'
	protocolname2 = 'udp'
	for port in range(1000000):
		try:
			#80 http 443 https
			print "TcpPort: %s => service name: %s" %(port, socket.getservbyport(port,protocolname1))
			print "			UdpPort: %s => service name: %s" %(port, socket.getservbyport(port,protocolname2))
		except Exception, e:
			pass
		
	print "Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp'))

# get_hostname()
#get_hostbyname()
# get_remote_machine_info()
#find_service_name()



import sys
import socket
import argparse
def main():
	print "s"
	# setup argument parsing
	parser = argparse.ArgumentParser(description='Socket Error Examples')
	parser.add_argument('--host', action="store", dest="host", required=False)
	parser.add_argument('--port', action="store", dest="port", type=int, required=False)
	parser.add_argument('--file', action="store", dest="file", required=False)
	given_args = parser.parse_args()
	host = given_args.host
	port = given_args.port
	#host = 'www.python.org'
	#port = 79

	filename = given_args.file
	# First try-except block -- create socket
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error, e:
		print "Error creating socket: %s" % e
		sys.exit(1)
	
	# Second try-except block -- connect to given host/port
	try:
		host = 'www.baidu.org'
		port = 80
		s.connect((host, port))
	except socket.gaierror, e:
		print "Address-related error connecting to server: %s" % e
		sys.exit(1)
	except socket.error, e:
		print "Connection error: %s" % e
		sys.exit(1)
	
	# Third try-except block -- sending data
	try:
		pass
		s.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)
	except socket.error, e:

		print "Error sending data: %s" % e
		sys.exit(1)
	
	while 1:
		# Fourth tr-except block -- waiting to receive data from remote host
		try:
			buf = s.recv(2048)
		except socket.error, e:
			print "Error receiving data: %s" % e
			sys.exit(1)
		if not len(buf):
			break
		# write the received data
		sys.stdout.write(buf)
#main()

#change buffer size
SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096
def modify_buff_size():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
	# Get the size of the socket's send buffer
	bufsize = [sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF),sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)]
	print "Buffer size [Before]:%s" %bufsize
	sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
	sock.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,SEND_BUF_SIZE)
	sock.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,RECV_BUF_SIZE)
	bufsize = [sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF),sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)]
	print "Buffer size [After]:%s"%bufsize
#modify_buff_size()

def test_socket_modes():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setblocking(1)#0 is non-block
	s.settimeout(0.5)
	s.bind(("127.0.0.1", 0))
	socket_address = s.getsockname()
	print "Trivial Server launched on socket: %s" %str(socket_address)
	while(1):
		s.listen(1)
#test_socket_modes()


import socket
import sys
def reuse_socket_addr():
	sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	# Get the old state of the SO_REUSEADDR option
	old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
	print "Old sock state: %s" %old_state
	# Enable the SO_REUSEADDR option, so we can use the port again
	sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
	new_state = sock.getsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR )
	print "New sock state: %s" %new_state
	local_port = 8282
	srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	# srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
	srv.bind( ('', local_port) )
	srv.listen(1)
	print ("Listening on port: %s " %local_port)
	while True:
		try:
			connection, addr = srv.accept()
			print 'Connected by %s:%s' % (addr[0], addr[1])
		except KeyboardInterrupt:
			break
		except socket.error, msg:
			print '%s' % (msg,)
# reuse_socket_addr()

import ntplib
from time import ctime
def print_time():
	ntp_client = ntplib.NTPClient()
	response = ntp_client.request('pool.ntp.org')

	print ctime(response.tx_time)
#print_time()


import socket
import struct
import sys
import time
NTP_SERVER = "0.uk.pool.ntp.org"
TIME1970 = 2208988800L

def sntp_client():
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	data = '\x1b' + 47 * '\0'
	client.sendto(data, (NTP_SERVER, 123))
	data, address = client.recvfrom( 1024 )
	if data:
		print 'Response received from:', address
	t = struct.unpack( '!12I', data )[10]
	t -= TIME1970
	print '\tTime=%s' % time.ctime(t)
#sntp_client()



import socket
import sys
import argparse
host = 'localhost'
def echo_client(port):
	""" A simple echo client """
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Connect the socket to the server
	server_address = (host, port)
	print "Connecting to %s port %s" % server_address
	sock.connect(server_address)
	# Send data
	try:
		# Send data
		message = "Test message. This will be echoed"
		print "Sending %s" % message
		sock.sendall(message)
		# Look for the response
		amount_received = 0
		amount_expected = len(message)
		while amount_received < amount_expected:
			data = sock.recv(16)
			amount_received += len(data)
			print "Received: %s" % data
	except socket.errno, e:
		print "Socket error: %s" %str(e)
	except Exception, e:
		print "Other exception: %s" %str(e)
	finally:
		print "Closing connection to the server"
	sock.close()
parser = argparse.ArgumentParser(description='Socket Server Example')
parser.add_argument('--port', action="store", dest="port", type=int,
required=True)
given_args = parser.parse_args()
port = given_args.port
echo_client(port)



