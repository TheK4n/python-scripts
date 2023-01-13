from totp import TOTP
import time


def client():
    totp = TOTP(5196600531324618753727604398109882003215613287302070736732575653427837252397175341587486155884671395499323786086015198694337784948422980111470315350336304)

    print("Client\n")
    while 1:
        code_in_hex = str(hex(totp.generate_onetime_code())).upper()[2:]
        print("Code:", code_in_hex)

        print("Code valid:", totp.get_rest_of_code_lifetime(), "seconds")

        time.sleep(1)


if __name__ == "__main__":
    client()
