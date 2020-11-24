from download_steamdb import save_steamdb_to_disk
from utils import get_steamdb_filename


def filter_steamdb_document(lines):
    return [l for l in lines if l.startswith('<a href="/app/')]


def parse_steamdb_app_id(line):
    return int(line.split('/')[2])


def load_steamdb_ranking():
    save_steamdb_to_disk()
    with open(get_steamdb_filename(), 'r', encoding='utf8') as f:
        d = f.readlines()
    steamdb_ranking = [parse_steamdb_app_id(l) for l in filter_steamdb_document(d)]
    print('[SteamDB] #apps = {}'.format(len(steamdb_ranking)))
    return steamdb_ranking


def main():
    steamdb_ranking = load_steamdb_ranking()
    return True


if __name__ == '__main__':
    main()
