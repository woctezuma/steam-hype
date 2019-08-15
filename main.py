import json
import time

import requests


def get_steam_hype_url():
    # This is not my API. Please use with moderation!

    url = 'https://steamhype-api.herokuapp.com/calendar'

    return url


def get_time_stamp():
    time_stamp = int(time.time() * 1000)

    return time_stamp


def get_steam_hype_params(num_followers=0):
    params = dict()

    params['start'] = get_time_stamp()
    params['current'] = 0
    params['followers'] = num_followers
    params['includedlc'] = 'false'
    params['price'] = 100
    params['discount'] = 0
    params['reviews'] = 0
    params['score'] = 0

    return params


def request_data(params=None):
    if params is None:
        params = get_steam_hype_params()

    resp_data = requests.get(url=get_steam_hype_url(),
                             params=params)

    result = resp_data.json()

    return result


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


def batch_request_data(params,
                       verbose=False):
    results = dict()

    while True:
        print('Request n°{}'.format(params['current'] + 1))

        result = request_data(params)

        if len(result) == 0:
            break
        else:
            for game in result:
                app_id = game['id']
                results[app_id] = game

            params['current'] += 1

    if verbose:
        print(results)

    save_results(results=results,
                 file_name=get_output_file_name())

    return results


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
    return


def main():
    load_from_disk = True,

    num_followers = 8000
    params = get_steam_hype_params(num_followers=num_followers)

    if load_from_disk:
        results = load_results()
    else:
        results = batch_request_data(params=params)

    print_formatted_results(results)

    return True


if __name__ == '__main__':
    main()
