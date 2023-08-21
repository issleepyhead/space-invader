from socket import socket
from networking.Packet import Packet

class Server(socket):
    """Socket class for game networking"""

    # sending packets
    def send(self, packet:Packet):
        pass

    def recieve(self):
        pass

    def open(self):
        pass

    def close(self):
        pass


