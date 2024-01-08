from typing import NoReturn
from common import BroadcastUDPSocket
import sys


class Broadcaster:
    def __init__(self, sock: BroadcastUDPSocket):
        self.sock = sock

    def send(self, message: bytes, broadcast_socket: tuple[str, int]) -> None:
        self.sock.sendto(message, broadcast_socket)

    def listen(self) -> NoReturn:
        counter = 0

        while True:
            data, addr = self.sock.recvfrom(1024)
            if data == b"pong":
                counter += 1
                print(addr[0])


if __name__ == "__main__":
    UDP_IP = "10.1.0.255"
    UDP_PORT = 55990
    MESSAGE = b"ping"

    sock = BroadcastUDPSocket()

    broadcaster = Broadcaster(sock)

    print(f"* Sent broadcast to {UDP_IP}:{UDP_PORT}", file=sys.stderr)
    broadcaster.send(MESSAGE, (UDP_IP, UDP_PORT))

    print(f"* Now listening {UDP_IP}:{UDP_PORT}...", file=sys.stderr)
    broadcaster.listen()
