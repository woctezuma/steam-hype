import time

import requests

from utils import save_results


def get_steam_hype_url():
    # This is not my API. Please use with moderation!

    url = 'https://steamhype-api.herokuapp.com/calendar'

    return url


def get_time_stamp():
    time_stamp = int(time.time() * 1000)

    return time_stamp


def get_steam_hype_params(num_followers=0):
    params = {}

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

    resp_data = requests.get(url=get_steam_hype_url(), params=params)

    result = resp_data.json()

    return result


def batch_request_data(params, save_results_to_disk=True, verbose=False):
    results = {}

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

    if save_results_to_disk:
        save_results(results=results)

    return results


def main(num_followers=5000, save_results_to_disk=True):
    params = get_steam_hype_params(num_followers=num_followers)

    results = batch_request_data(
        params=params,
        save_results_to_disk=save_results_to_disk,
    )

    return True


if __name__ == '__main__':
    main()
