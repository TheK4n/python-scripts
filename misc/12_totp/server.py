from totp import TOTP


def server():
    totp = TOTP(5196600531324618753727604398109882003215613287302070736732575653427837252397175341587486155884671395499323786086015198694337784948422980111470315350336304)

    print("Server\n")

    while 1:
        try:
            code_in_hex = int(input("Key: "), base=16)
        except ValueError:
            print("Wrong code format!")
        else:
            print("Access", "approved" if totp.verify_onetime_code(code_in_hex) else "denied")


if __name__ == "__main__":
    server()

