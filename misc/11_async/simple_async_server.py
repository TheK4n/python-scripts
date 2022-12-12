import socket
import selectors
import json


selector = selectors.DefaultSelector()


class ResponseFormatter:

    @staticmethod
    def join_headers(*headers):
        r"""Join headers by \r\n and \n\n in end"""
        headers = list(headers)
        headers.append("Content-Type: application/json; charset=utf-8")
        return "\r\n".join(headers) + "\n\n"


class ResponseGenerator:

    def __init__(self):
        self.__routes = {}

    def add_route(self, path: str, handler: callable):
        self.__routes[path] = handler

    def __generate_content(self, code: int, path: str) -> str:
        if code == 404:
            return '{"status": "Not found"}'
        if code == 405:
            return '{"status": "Not allowed"}'
        return json.dumps(self.__routes[path]())

    def __generate_headers(self, method: str, path: str) -> (str, int):

        response_formatter = ResponseFormatter()

        if method != "GET":
            return response_formatter.join_headers("HTTP/1.1 405 Method not allowed"), 405

        if path not in self.__routes:
            return response_formatter.join_headers("HTTP/1.1 404 Not found"), 404

        return response_formatter.join_headers("HTTP/1.1 200 OK"), 200

    def generate_by_path(self, method: str, path: str):
        headers, code = self.__generate_headers(method, path)
        body = self.__generate_content(code, path)
        return (headers + body).encode("utf-8")


class RequestParser:

    @staticmethod
    def parse(request: bytes) -> (str, str):
        try:
            method, path, *_ = request.decode("utf-8").split(" ")
        except ValueError:
            return "GET", "/"
        return method.strip(), path.strip()


class Server:
    def __init__(self,
                 socket_params = ("localhost", 8000)):
        self._socket_params = socket_params
        self._response_generator = ResponseGenerator()

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET - ipv4, SOCK_STREAM - tcp
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # set option: re-use addr True

        selector.register(fileobj=self.server_socket, events=selectors.EVENT_READ, data=self.__accept_connection)


    def add_route(self, path: str, handler: callable):
        self._response_generator.add_route(path, handler)

    def __listen(self):
        self.server_socket.bind(self._socket_params)
        self.server_socket.listen()
        print("Server started at", *self._socket_params)

    def __accept_connection(self, server_socket):
        client_socket, addr = server_socket.accept()
        print("Accept from", *addr)

        selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=self.__handle_client)

    def __handle_client(self, client_socket):
        request = client_socket.recv(4096)

        if request:
            request_parser = RequestParser()

            method, path = request_parser.parse(request)

            response = self._response_generator.generate_by_path(method, path)
            client_socket.sendall(response)
        selector.unregister(client_socket)
        client_socket.close()

    def start_polling(self):

        self.__listen()

        while True:
            events = selector.select()

            for key, _ in events:
                callback = key.data
                callback(key.fileobj)


def route_root():
    return {"status": "ok"}

def calculate_some():
    return {"result": 200+200}


if __name__ == "__main__":
    server = Server()
    server.add_route("/", route_root)
    server.add_route("/calc", calculate_some)
    server.start_polling()

