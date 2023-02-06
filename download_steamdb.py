from pathlib import Path

import requests

from utils import get_steamdb_filename


def get_steamdb_url():
    return 'https://steamdb.info/upcoming/?hype'


def get_headers():
    # To avoid status code 403 ("Forbidden"):
    return {'user-agent': 'my-app/0.0.1'}


def download_steamdb():
    text_aggregate = ''
    r = requests.get(url=get_steamdb_url(), headers=get_headers())
    if r.ok:
        text_aggregate = r.text
    return text_aggregate


def save_steamdb_to_disk():
    if not Path(get_steamdb_filename()).exists():
        text_aggregate = download_steamdb()
        if len(text_aggregate) > 0:
            with open(get_steamdb_filename(), 'w', encoding='utf8') as f:
                f.write(text_aggregate)
    return True


def main():
    save_steamdb_to_disk()
    return True


if __name__ == '__main__':
    main()
