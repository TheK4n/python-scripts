import socket


class BroadcastUDPSocket(socket.socket):
    def __init__(self, *args, **kwargs):
        super().__init__(socket.AF_INET, socket.SOCK_DGRAM, *args, **kwargs)
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
