import json
import base64
import hmac
from hashlib import sha256


def b64urlsafe_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("utf-8").replace("=", "")


class JWTValidationError(Exception):
    pass


class JWT:
    def __init__(self, token: str):
        self.__token = token
        self.__validate()

    def __split_token(self) -> tuple[str, str, str]:
        return tuple(self.__token.split("."))

    def __validate(self):
        """Raises ValidateError if invalid token"""
        token_parts = self.__split_token()

        if len(token_parts) != 3:
            raise JWTValidationError("Current jwt is not valid")

        for e in token_parts:
            if len(e) < 1:
                raise JWTValidationError("Current jwt is not valid")

    def __to_dict(self) -> dict:
        _, encoded_payload, _ = self.__split_token()
        return json.loads(base64.urlsafe_b64decode((encoded_payload + "==").encode("utf-8")).decode("utf-8"))

    def __getitem__(self, key: str) -> str:
        """Returns value from payload by key"""

        try:
            return self.__to_dict()[key]
        except KeyError:
            raise KeyError(f"Jwt payload hasnt current key: {key}")


    def __str__(self) -> str:
        return self.__token

    def verify(self, secret: str) -> bool:
        header, payload, sign = self.__split_token()

        h = hmac.new(secret.encode("utf-8"), f"{header}.{payload}".encode("utf-8"), sha256)

        new_sign = b64urlsafe_encode(h.digest())

        return new_sign == sign


class JWTGenerator:
    def __init__(self, secret: str, header: dict[str, str] | None = None):
        self.__secret = secret

        if header is None:
            self._header = {
                "alg": "HS256",
                "typ": "JWT"
            }
        else:
            self._header = header
        self.__header_encoded = b64urlsafe_encode(json.dumps(self._header).encode("utf-8"))

    def _get_token_sign(self, payload_encoded: str) -> bytes:
        h = hmac.new(self.__secret.encode("utf-8"), f"{self.__header_encoded}.{payload_encoded}".encode("utf-8"), sha256)
        return h.digest()

    def generate(self, payload: dict[str, str]) -> JWT:
        payload_encoded = b64urlsafe_encode(json.dumps(payload).encode("utf-8"))
        sign_encoded = b64urlsafe_encode(self._get_token_sign(payload_encoded))
        token = ".".join([self.__header_encoded, payload_encoded, sign_encoded])
        return JWT(token)


if __name__ == '__main__':
    SECRET = "secret"
    LOGIN = "kan"

    jwt = JWTGenerator(SECRET).generate({"login": LOGIN})
    assert jwt.verify(SECRET)
    assert jwt["login"] == LOGIN

