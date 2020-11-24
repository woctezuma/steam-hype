from download_steam import save_steam_to_disk
from utils import get_steam_filename


def filter_steam_document(lines):
    return [l for l in lines if 'data-ds-appid' in l]


def parse_steam_app_id(line):
    element = next(e for e in line.split() if 'data-ds-appid' in e)
    return int(element.split('"')[1])


def load_steam_ranking():
    save_steam_to_disk()
    with open(get_steam_filename(), 'r', encoding='utf8') as f:
        d = f.readlines()
    steam_ranking = [parse_steam_app_id(l) for l in filter_steam_document(d)]
    print('[Steam] #apps = {}'.format(len(steam_ranking)))
    return steam_ranking


def main():
    steam_ranking = load_steam_ranking()
    return True


if __name__ == '__main__':
    main()
