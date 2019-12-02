import socket, sys

if len(sys.argv) == 3:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.connect(('127.0.0.1', 62300))
	s.send(f'{sys.argv[1]} {sys.argv[2]}'.encode())
	s.close()
