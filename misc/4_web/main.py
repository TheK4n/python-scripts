import requests as requests


def download_file(url, filename, chunk_size=8192):
    """Saves file to folder from url"""
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as file:
        for chunk in r.iter_content(chunk_size):
            file.write(chunk)


def get_html(url, useragent=None, proxy=None):
    return requests.get(url, headers=useragent, proxies=proxy).text

