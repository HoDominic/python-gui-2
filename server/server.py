from pathlib import Path
import sys
import logging
import socket
import threading
print(sys.path[0])  # test
sys.path[0] = str(Path(sys.path[0]).parent)  # Hier aanpassen
print(sys.path[0])

#from server.clienthandler import ClientHandler
from server.clienthandler import ClientHandler
from pathlib import Path





# create a socket object


logging.basicConfig(level=logging.DEBUG)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

# bind to the port
serversocket.bind((host, port))


# queue up to 5 requests
serversocket.listen(5)

while True:
    logging.info("Server: waiting for a client...")

    # establish a connection
    socket_to_client, addr = serversocket.accept()

    logging.info(f"Server: Got a connection from {addr})")
    clh = ClientHandler(socket_to_client)
    clh.start()
    logging.info(
        f"Server: ok, clienthandler started. Current Thread count: {threading.active_count()}.")
