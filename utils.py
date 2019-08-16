import json


def get_data_folder():
    folder_name = 'data/'

    return folder_name


def get_output_file_name():
    file_name = get_data_folder() + 'upcoming_games.json'

    return file_name


def load_results(file_name=None,
                 verbose=True):
    if file_name is None:
        file_name = get_output_file_name()

    with open(file_name, 'r') as f:
        results = json.load(f)

    if verbose:
        print('Loading {} games.'.format(len(results)))

    return results


def save_results(results,
                 file_name=None,
                 verbose=True):
    if file_name is None:
        file_name = get_output_file_name()

    with open(file_name, 'w') as f:
        json.dump(results, f)

    if verbose:
        print('Saving {} games.'.format(len(results)))

    return


def get_steamdb_url(app_id):
    url = 'https://steamdb.info/app/' + str(app_id) + '/'

    return url


def print_formatted_results(results):
    sorted_app_ids = sorted(results.keys(),
                            key=lambda x: results[x]['steam_followers'],
                            reverse=True)

    for (rank, app_id) in enumerate(sorted_app_ids):
        game = results[app_id]
        print('{:3}) {} (appID=[{}]({}) ; #followers = {})'.format(rank + 1,
                                                                   game['title'],
                                                                   game['id'],
                                                                   get_steamdb_url(app_id),
                                                                   game['steam_followers']))
    return True


def main():
    results = load_results()

    print_formatted_results(results)

    return True


if __name__ == '__main__':
    main()
