import json
import os
import hashlib
from random import randint


class Corrupted(Exception):
    pass


class Blockchain:

    def __init__(self):
        self.BC_dir = os.path.join(os.curdir, 'blocks')
        if not os.path.exists(self.BC_dir):
            os.mkdir(self.BC_dir)

        files = self.get_files()

        if len(files) == 0:
            self.__write_genesis()

    def check_integrity(self):
        return self.__get_corr_blocks()

    @staticmethod
    def __get_hash(data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()

    def get_hash(self, filename):
        """
        Returns md5 hash of file
        """
        data = open(os.path.join(self.BC_dir, filename), 'rb').read().decode()
        return self.__get_hash(data)

    def get_files(self):
        """
        Return sorted files in directory
        """

        files = os.listdir(self.BC_dir)
        return sorted(files, key=int)

    def __get_corr_blocks(self) -> list[str]:
        """
        Returns list of corrupted files
        """

        result = []
        files = self.get_files()

        for file in files[1:]:
            with open(os.path.join(self.BC_dir, file)) as f:
                h = json.load(f)['hash']
            prev_file = str(int(file) - 1)
            try:
                actual_hash = self.get_hash(prev_file)
            except FileNotFoundError:
                result.append(prev_file)
                return result
            if h != actual_hash:
                result.append(prev_file)

        return result

    def __write_json(self, filename: str, data: dict):
        with open(os.path.join(self.BC_dir, filename), 'w') as file:
            file.write(json.dumps(data))

    def __write_genesis(self):
        data = {
            'name': 'genesis',
            'hash': None
        }

        data.update({"pow": self.__find_pow(data)})

        self.__write_json('0', data)

    def __find_pow(self, local_data: dict, difficult: int = 4) -> int:
        chars = "0" * difficult
        pow_number = randint(100, 1000000)
        while True:
            local_data.update({"pow": pow_number})
            if self.__get_hash(json.dumps(local_data)).startswith(chars):
                return pow_number
            pow_number += 1

    def write_block(self, data: dict):
        files = self.get_files()
        prev_file = files[-1]

        prev_hash = self.get_hash(prev_file)
        data.update({'hash': prev_hash})  # add hash in end of 2_json
        data.update({"pow": self.__find_pow(data)})

        corrupted = self.__get_corr_blocks()
        if corrupted:
            raise Corrupted(corrupted)

        prev_file = self.get_files()[-1]
        filename = str(int(prev_file) + 1)

        self.__write_json(filename, data)


def add_some_blocks(bc: Blockchain):
    creditors = {'danya': 300, 'anya': 2000, 'pasha': 800, 'vasya': 100}
    for k, v in creditors.items():
        bc.write_block({'name': k, "amount": v, "to": "me"})


if __name__ == '__main__':
    BC = Blockchain()
    # add_some_blocks(BC)
    print(BC.check_integrity())
