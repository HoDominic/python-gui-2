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

# https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
import logging
from random import choices
import socket
from tkinter import *

from tkinter import messagebox
from tkinter.ttk import Combobox


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        # Functies oproepen!
        self.init_window()
        #self.makeConnnectionWithServer()

    # Creation of init_window
    def init_window(self):
        self.master.title("Admin GUI")
        self.master.geometry("350x150")
        self.master.resizable(False, False)

        # root.protocol("WM_DELETE_WINDOW", _delete_window)

    def __del__(self):
        self.close_connection()

    def makeConnnectionWithServer(self):
        try:
            logging.info("Making connection with server...")
            # get local machine name
            host = socket.gethostname()
            port = 9999
            self.socket_to_server = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            # connection to hostname on the port.
            self.socket_to_server.connect((host, port))
            self.my_writer_obj = self.socket_to_server.makefile(mode='rw')
            logging.info("Open connection with server succesfully")
        except Exception as ex:
            logging.error(f"Foutmelding: {ex}")

    def calculateStopafstand(self):
        try:
            snelheid = int(self.entry_snelheid.get())/3.6
            reactietijd = int(self.entry_reactietijd.get())

            wegdek = (self.cbo_wegdek.get())

            if wegdek == "Droog wegdek":
                wegdek = 5
            else:
                wegdek = 8

            print(type(wegdek))

            self.my_writer_obj.write(f"{snelheid}\n")
            logging.info(f"Sending snelheid: {snelheid}")

            self.my_writer_obj.write("%s\n" % reactietijd)
            logging.info(f"Sending reactietijd: {reactietijd}")

            self.my_writer_obj.write("%s\n" % wegdek)
            logging.info(f"Sending wegdek: {wegdek}")

            self.my_writer_obj.flush()

            # waiting for answer
            answer = self.my_writer_obj.readline().rstrip('\n')
            logging.info(f"Answer server: {answer}")
            stopafstand = int(answer)

            self.label_resultaat['text'] = f"{stopafstand}"

        except Exception as ex:
            logging.error(f"Foutmelding: {ex}")
            messagebox.showinfo("Stopafstand berekenen",
                                "Something has gone wrong...")

    def close_connection(self):
        try:
            logging.info("Close connection with server...")
            self.my_writer_obj.write("CLOSE\n")
            self.my_writer_obj.flush()
            self.socket_to_server.close()
        except Exception as ex:
            logging.error(f"Foutmelding: {ex}")
            messagebox.showinfo("Stopafstand berekenen",
                                "Something has gone wrong...")


logging.basicConfig(level=logging.INFO)

root = Tk()
# root.geometry("400x300")
app = Window(root)
root.mainloop()

while True:
    logging.info("Server: waiting for a client...")

    # establish a connection
    socket_to_client, addr = serversocket.accept()

    logging.info(f"Server: Got a connection from {addr})")
    clh = ClientHandler(socket_to_client)
    clh.start()
    logging.info(
        f"Server: ok, clienthandler started. Current Thread count: {threading.active_count()}.")

