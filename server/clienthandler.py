import logging
import threading

from matplotlib.patches import Wedge


class ClientHandler(threading.Thread):

    def __init__(self, socketclient):
        threading.Thread.__init__(self)
        self.socket_to_client = socketclient

    def run(self):
       # io_stream_client = self.socket_to_client.makefile(mode='rw')



        #CATCH LOGIN client_to_server messge after login from client-side 
   
        io_stream_client = self.socket_to_client.makefile(mode='rw')
        io_stream_client.write("Thank you for connecting!\n")       #newline karakter niet vergeten!
        io_stream_client.flush()


        logging.info("CLH - started & waiting...")
        commando = io_stream_client.readline().rstrip('\n')
        while commando != "CLOSE":
            snelheid = io_stream_client.readline().rstrip('\n')
            logging.debug(f"CLH - snelheid: {snelheid}")
            reactietijd = io_stream_client.readline().rstrip('\n')
            logging.debug(f"CLH - reactietijd: {reactietijd}")

            #wegdek = io_stream_client.readline().rstrip('\n')
            #logging.debug(f"CLH - wegdek: {wegdek}")

            berekening = str(snelheid) + str(reactietijd)
            # (int(snelheid) * int(reactietijd)) + \
            #   int(snelheid*snelheid) / int(float(wegdek * 2))
            io_stream_client.write(f"{berekening}\n")
            io_stream_client.flush()
            logging.debug(f"CLH - Sending back stopafstand: {berekening}")

            commando = io_stream_client.readline().rstrip('\n')

        logging.debug(f"CLH - Connection closed...")
        self.socket_to_client.close()
