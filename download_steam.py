from pathlib import Path

import requests

from utils import get_steam_filename


def get_steam_url(page_no=1):
    url = 'https://store.steampowered.com/search/?filter=popularwishlist&page={}'
    return url.format(page_no)


def download_steam(num_pages=10):
    text_aggregate = ''

    # We download 10 pages with 25 games per page, for a total of 250 games.
    for page_no in range(num_pages):
        r = requests.get(url=get_steam_url(1 + page_no))
        if r.ok:
            text_aggregate += r.text

    return text_aggregate


def save_steam_to_disk(num_pages=10):
    if not Path(get_steam_filename()).exists():
        text_aggregate = download_steam(num_pages=num_pages)
        if len(text_aggregate) > 0:
            with open(get_steam_filename(), 'w', encoding='utf8') as f:
                f.write(text_aggregate)
    return True


def main():
    save_steam_to_disk()


if __name__ == '__main__':
    main()
