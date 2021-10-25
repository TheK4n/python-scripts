import json
import os
import hashlib


class Corrupted(Exception):
    pass


class Blockchain:

    def __init__(self):
        self.BC_dir = os.path.join(os.curdir, 'blockchain')
        if not os.path.exists(self.BC_dir):
            os.mkdir(self.BC_dir)

        files = self.get_files()

        if len(files) == 0:
            self.__write_genesis()

    @property
    def corrupted_blocks(self):
        return self.__get_corr_blocks()

    def get_hash(self, filename):
        """
        Returns md5 hash of file
        """
        file = open(os.path.join(self.BC_dir, filename), 'rb').read()
        return hashlib.md5(file).hexdigest()

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
            actual_hash = self.get_hash(prev_file)

            if h != actual_hash:
                result.append(prev_file)

        return result

    def __write_json(self, filename: str, data: dict):
        with open(os.path.join(self.BC_dir, filename), 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def __write_plug(self):
        prev_file = self.get_files()[-1]
        filename = str(int(prev_file) + 1)
        self.__write_json(filename, {"name": "plug", "hash": self.get_hash(prev_file)})

    def __write_genesis(self):
        data = {
            'name': 'genesis',
            'hash': None
        }

        self.__write_json('0', data)
        self.__write_plug()

    def write_block(self, data: dict):
        files = self.get_files()
        prev_file = files[-2]  # last file exclusive of plug file

        prev_hash = self.get_hash(prev_file)
        data.update({'hash': prev_hash})  # add hash in end of json

        corrupted = self.__get_corr_blocks()
        if corrupted:
            raise Corrupted(corrupted)
        self.__write_json(files[-1], data)  # rewrite plug file
        self.__write_plug()


def add_some_blocks(bc: Blockchain):
    creditors = {'danya': 300, 'anya': -2000, 'pasha': 800, 'vasya': 100}
    for k, v in creditors.items():
        bc.write_block({'name': k, "amount": v, "to": "me"})


if __name__ == '__main__':
    BC = Blockchain()
    add_some_blocks(BC)
    print(BC.corrupted_blocks)
