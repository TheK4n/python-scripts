import json
import os
import hashlib

if not os.path.exists('blockchain'):
    os.mkdir('blockchain')

BC_dir = os.curdir + '/blockchain/'


def get_hash(filename):
    file = open(BC_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()


def get_files():
    files = os.listdir(BC_dir)
    return sorted(files, key=int)


def get_corr_blocks():
    is_corrupted = False

    result = []
    files = get_files()

    for file in files[1:]:
        with open(BC_dir + str(file)) as f:
            h = json.load(f)['hash']
        prev_file = str(int(file) - 1)
        actual_hash = get_hash(prev_file)

        if h != actual_hash:
            result.append(prev_file)
            is_corrupted = True

    if is_corrupted:
        return result
    else:
        return False


def write_genesis():
    data = {
        'name': 'genesis',
        'amount': None,
        'to': None,
        'hash': None
    }

    with open(BC_dir + '1', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def write_block(name, amount, to, prev_hash=''):
    files = get_files()

    if len(files) == 0:
        write_genesis()

    files = get_files()
    prev_file = files[-1]

    filename = str(int(files[-1]) + 1)

    prev_hash = get_hash(str(prev_file))
    data = {
        'name': name,
        'amount': amount,
        'to': to,
        'hash': prev_hash
    }

    with open(BC_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    creditors = {'danya': 300, 'anya': -2000, 'pasha': 800, 'vasya': 100}
    for k, v in creditors.items():
        write_block(k, v, 'me')
    print(get_corr_blocks())


if __name__ == '__main__':
    main()