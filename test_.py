import unittest

import compare_to_top_wishlists
import download_hype
import download_steam
import download_steamdb
import parse_steam
import parse_steamdb
import utils


class TestParseSteamMethods(unittest.TestCase):
    def test_filter_steam_document(self):
        lines = ['nope', 'blabla data-ds-appid="1091500" blabla', 'nope']
        filtered_lines = parse_steam.filter_steam_document(lines)
        self.assertEqual(len(lines), 3)
        self.assertEqual(len(filtered_lines), 1)

    def test_parse_steam_app_id(self):
        line = 'blabla data-ds-appid="1091500" blabla'
        app_id = parse_steam.parse_steam_app_id(line)
        self.assertEqual(app_id, 1091500)

    def test_load_steam_ranking(self):
        ranking = parse_steam.load_steam_ranking()
        self.assertEqual(len(ranking), 250)

    def test_main(self):
        self.assertTrue(parse_steam.main())


class TestParseSteamDBMethods(unittest.TestCase):
    def test_filter_steamdb_document(self):
        lines = ['nope', '<a href="/app/1091500/" class="b">Cyberpunk 2077</a>', 'nope']
        filtered_lines = parse_steamdb.filter_steamdb_document(lines)
        self.assertEqual(len(lines), 3)
        self.assertEqual(len(filtered_lines), 1)

    def test_parse_steamdb_app_id(self):
        line = '<a href="/app/1091500/" class="b">Cyberpunk 2077</a>'
        app_id = parse_steamdb.parse_steamdb_app_id(line)
        self.assertEqual(app_id, 1091500)

    def test_load_steamdb_ranking(self):
        ranking = parse_steamdb.load_steamdb_ranking()
        self.assertEqual(len(ranking), 250)

    def test_main(self):
        self.assertTrue(parse_steamdb.main())


class TestDownloadSteamMethods(unittest.TestCase):
    def test_get_steam_url(self):
        url = download_steam.get_steam_url()
        self.assertGreater(len(url), 0)

    def test_download_steam(self):
        text_aggregate = download_steam.download_steam(num_pages=1)
        self.assertGreater(text_aggregate, 0)

    def test_save_steam_to_disk(self):
        self.assertTrue(download_steam.save_steam_to_disk(num_pages=1))

    def test_main(self):
        self.assertTrue(download_steam.main())


class TestDownloadSteamDBMethods(unittest.TestCase):

    def test_get_steamdb_url(self):
        url = download_steamdb.get_steamdb_url()
        self.assertGreater(len(url), 0)

    def test_get_headers(self):
        headers = download_steamdb.get_headers()
        self.assertIn('user-agent', headers)
        self.assertGreater(len(headers['user-agent']), 0)

    def test_download_steamdb(self):
        text_aggregate = download_steamdb.download_steamdb()
        self.assertGreater(text_aggregate, 0)

    def test_save_steamdb_to_disk(self):
        self.assertTrue(download_steamdb.save_steamdb_to_disk())

    def test_main(self):
        self.assertTrue(download_steamdb.main())


class TestUtilsMethods(unittest.TestCase):

    def test_get_steamdb_url(self):
        url = utils.get_steamdb_url(app_id='440')
        self.assertGreater(len(url), 0)

    def test_get_data_folder(self):
        folder_name = utils.get_data_folder()
        self.assertGreater(len(folder_name), 0)

    def test_get_data_folder_v2(self):
        folder_name = utils.get_data_folder(version=2)
        self.assertEqual(folder_name, 'data_v2/')

    def test_get_steam_filename(self):
        file_name = utils.get_steam_filename()
        self.assertTrue(file_name.endswith('steam.txt'))

    def test_get_steamdb_filename(self):
        file_name = utils.get_steamdb_filename()
        self.assertTrue(file_name.endswith('steamdb.txt'))

    def test_get_output_file_name(self):
        file_name = utils.get_output_file_name()
        self.assertGreater(len(file_name), 0)

    def test_get_manual_wishlist_snapshot_file_name(self):
        file_name = utils.get_manual_wishlist_snapshot_file_name()
        self.assertGreater(len(file_name), 0)

    def test_load_json(self):
        file_name = utils.get_output_file_name()
        loaded_data = utils.load_json(file_name, verbose=True)
        self.assertGreater(len(loaded_data), 0)

    def test_load_manual_wishlist_snapshot(self):
        manual_wishlist_snapshot = utils.load_manual_wishlist_snapshot()
        self.assertGreater(len(manual_wishlist_snapshot), 0)

    def test_load_results(self):
        results = utils.load_results()
        self.assertGreater(len(results), 0)

    def test_save_results(self):
        results = utils.load_results()

        temp_file_name = utils.get_data_folder() + 'temp.json'
        utils.save_results(results, file_name=temp_file_name)

        temp = utils.load_results(file_name=temp_file_name)
        self.assertEqual(results, temp)

    def test_sort_by_followers(self):
        results = utils.load_results()
        app_ids = utils.sort_by_followers(results)

        self.assertGreater(len(app_ids), 0)

        first_amount = results[str(app_ids[0])]['steam_followers']
        last_amount = results[str(app_ids[-1])]['steam_followers']

        self.assertGreaterEqual(int(first_amount), int(last_amount))

    def test_print_formatted_results(self):
        results = utils.load_results()
        self.assertTrue(utils.print_formatted_results(results))

    def test_main(self):
        self.assertTrue(utils.main())


class TestDownloadHypeMethods(unittest.TestCase):

    def test_get_steam_hype_url(self):
        url = download_hype.get_steam_hype_url()
        self.assertGreater(len(url), 0)

    def test_get_time_stamp(self):
        time_stamp = download_hype.get_time_stamp()
        self.assertGreater(time_stamp, 0)

    def test_get_steam_hype_params(self):
        input_value = 8000
        params = download_hype.get_steam_hype_params(num_followers=input_value)
        self.assertEqual(params['followers'], input_value)

    def test_request_data(self):
        result = download_hype.request_data()
        self.assertGreater(len(result), 0)

    def test_batch_request_data(self):
        input_value = 100000
        params = download_hype.get_steam_hype_params(num_followers=input_value)
        results = download_hype.batch_request_data(params,
                                                   save_results_to_disk=False)
        self.assertGreater(len(results), 0)

    def test_main(self):
        input_value = 100000
        self.assertTrue(download_hype.main(num_followers=input_value,
                                           save_results_to_disk=False))


class TestCompareToTopWishlistsMethods(unittest.TestCase):

    def test_trim_rankings(self):
        ranking_A = range(10)
        ranking_B = range(20)

        ranking_A, ranking_B = compare_to_top_wishlists.trim_rankings(ranking_A,
                                                                      ranking_B)

        self.assertEqual(len(ranking_A), len(ranking_B))

    def test_compute_rho(self):
        ranking_A = [12, 2, 1, 12, 2]
        ranking_B = [1, 4, 7, 1, 0]

        rho, p_value = compare_to_top_wishlists.compute_rho(ranking_A,
                                                            ranking_B)

        self.assertTrue(-1 <= rho <= 1)

    def test_compute_tau(self):
        ranking_A = [12, 2, 1, 12, 2]
        ranking_B = [1, 4, 7, 1, 0]

        tau, p_value = compare_to_top_wishlists.compute_tau(ranking_A,
                                                            ranking_B)

        self.assertTrue(-1 <= tau <= 1)

    def test_compute_weighted_tau(self):
        ranking_A = [12, 2, 1, 12, 2]
        ranking_B = [1, 4, 7, 1, 0]

        weighted_tau, p_value = compare_to_top_wishlists.compute_weighted_tau(ranking_A,
                                                                              ranking_B)

        self.assertTrue(-1 <= weighted_tau <= 1)

    def test_compute_rank_biased_overlap(self):
        ranking_A = [12, 2, 1, 12, 2]
        ranking_B = [1, 4, 7, 1, 0]

        rbo_estimate, reference_overlap = compare_to_top_wishlists.compute_rank_biased_overlap(ranking_A,
                                                                                               ranking_B)

        self.assertTrue(0 <= rbo_estimate <= 1)
        self.assertTrue(0 <= reference_overlap <= 1)

    def test_compute_several_rank_correlations(self):
        ranking_A = [12, 2, 1, 12, 2]
        ranking_B = [1, 4, 7, 1, 0]

        self.assertTrue(compare_to_top_wishlists.compute_several_rank_correlations(ranking_A,
                                                                                   ranking_B))

    def test_main(self):
        self.assertTrue(compare_to_top_wishlists.main())


if __name__ == '__main__':
    unittest.main()
