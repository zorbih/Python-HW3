from socket import *
import threading
from Connector import Connector
import sys

def run_game():
	execfile("Textcraft.py")

def catch_incoming(client):
	c = Connector(client)
	sys.stdout = c
	sys.stdin = c
	t=threading.Thread(target=run_game)
	t.start()

if __name__ == "__main__":
	# Create IPv4 TCP socket
	s = socket(AF_INET, SOCK_STREAM)
	# Bind to localhost:9700
	s.bind(("",9700))
	s.listen(5)
	while True:
		c,a = s.accept()
		# Handle client connection in a new thread.
		catch_incoming(c)
