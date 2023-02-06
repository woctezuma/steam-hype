import json
from pathlib import Path


def get_data_folder(version=1):
    folder_name = 'data/'

    if version > 1:
        folder_name = 'data_v2/'

    Path(folder_name).mkdir(parents=True, exist_ok=True)

    return folder_name


def get_steam_filename(version=2):
    return get_data_folder(version=version) + 'steam.txt'


def get_steamdb_filename(version=2):
    return get_data_folder(version=version) + 'steamdb.txt'


def get_output_file_name():
    file_name = get_data_folder() + 'upcoming_games.json'

    return file_name


def get_manual_wishlist_snapshot_file_name():
    file_name = get_data_folder() + 'top_wishlists.json'

    return file_name


def load_json(file_name=None, verbose=False):
    with open(file_name) as f:
        data = json.load(f)

    if verbose:
        print(f'Loading {len(data)} games.')

    return data


def load_manual_wishlist_snapshot(file_name=None, verbose=True):
    if file_name is None:
        file_name = get_manual_wishlist_snapshot_file_name()

    manual_wishlist_snapshot = load_json(file_name=file_name, verbose=verbose)

    return manual_wishlist_snapshot


def load_results(file_name=None, verbose=True):
    if file_name is None:
        file_name = get_output_file_name()

    results = load_json(file_name=file_name, verbose=verbose)

    return results


def save_results(results, file_name=None, verbose=True):
    if file_name is None:
        file_name = get_output_file_name()

    with open(file_name, 'w') as f:
        json.dump(results, f)

    if verbose:
        print(f'Saving {len(results)} games.')

    return


def get_steamdb_url(app_id):
    url = 'https://steamdb.info/app/' + str(app_id) + '/'

    return url


def sort_by_followers(results=None):
    if results is None:
        results = load_results()

    sorted_app_ids = sorted(
        results.keys(),
        key=lambda x: results[x]['steam_followers'],
        reverse=True,
    )

    sorted_app_ids_as_integers = [int(app_id) for app_id in sorted_app_ids]

    return sorted_app_ids_as_integers


def print_formatted_results(results):
    sorted_app_ids = sort_by_followers(results)

    for rank, app_id in enumerate(sorted_app_ids):
        game = results[str(app_id)]
        print(
            '{:3}) {} (appID=[{}]({}) ; #followers = {})'.format(
                rank + 1,
                game['title'],
                game['id'],
                get_steamdb_url(app_id),
                game['steam_followers'],
            ),
        )
    return True


def main():
    results = load_results()

    print_formatted_results(results)

    return True


if __name__ == '__main__':
    main()
