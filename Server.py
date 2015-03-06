from socket import *
import threading
from Connector import Connector
import sys

def run_game(client):
	execfile("Textcraft.py")
	client.close()

def catch_incoming(client):
	c = Connector(client)
	sys.stdout = c
	sys.stdin = c
	t=threading.Thread(target=run_game, args=(client,))
	t.start()


if __name__ == "__main__":
	print "Launching server..."
	# Create IPv4 TCP socket
	s = socket(AF_INET, SOCK_STREAM)
	# Bind to localhost:9700
	s.bind(("",9700))
	s.listen(5)
	while True:
		c,a = s.accept()
		print "Accepting client."
		# Handle client connection in a new thread.
		catch_incoming(c)
