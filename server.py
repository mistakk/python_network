
import socket
import sys
def reuse_socket_addr():
	sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
	local_port = 444
	sock.bind( ("localhost", local_port) )
	sock.listen(1) 
	#the max client number the server can connent at same time 
	print ("Listening on port: %s " %local_port)
	while True:
		try:
			connection, addr = sock.accept()
			#the thread is block here for waitting connect
			print 'Connected by %s:%s' % (addr[0], addr[1])		
			#print the client message
			while True:
				data= connection.recv(1000)
				if not data:
					break
				message = "I am client and I have receive your message"
				connection.send(message)
				print "receive data: %s" %data
				print "send data:%s" %message
			connection.close()
		except Expection,ex:
			print ex
reuse_socket_addr()