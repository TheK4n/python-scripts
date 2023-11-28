from typing import NoReturn
from common import BroadcastUDPSocket


class Listener:
    def __init__(self, sock: BroadcastUDPSocket):
        self.sock = sock

    def is_valid_request(self, data: bytes) -> bool:
        return data == b"ping"

    def answer(self, receiver_addr: tuple[str, int]) -> None:
        self.sock.sendto(b"pong", receiver_addr)

    def answer_on_request(self) -> NoReturn:
        while True:
            data, addr = self.sock.recvfrom(1024)
            if self.is_valid_request(data):
                self.answer(addr)
                print(f"[O] received Valid request: {data}, {addr}")
            else:
                print(f"[X] received invalid request: {data}, {addr}")


if __name__ == "__main__":
    UDP_IP = "0.0.0.0"
    UDP_PORT = 55990

    sock = BroadcastUDPSocket()
    sock.bind((UDP_IP, UDP_PORT))

    listener = Listener(sock)
    listener.answer_on_request()
