import unittest
import main

class TestMainMethods(unittest.TestCase):

    def test_main(self):
        self.assertTrue(main.main())


if __name__ == '__main__':
    unittest.main()

