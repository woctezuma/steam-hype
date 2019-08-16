import unittest

import download_hype
import utils


class TestUtilsMethods(unittest.TestCase):

    def test_get_steamdb_url(self):
        url = utils.get_steamdb_url(app_id='440')
        self.assertGreater(len(url), 0)

    def test_get_data_folder(self):
        folder_name = utils.get_data_folder()
        self.assertGreater(len(folder_name), 0)

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


if __name__ == '__main__':
    unittest.main()
