import unittest
import unittest.mock as mock
from main_function import validation_with_try


class MyTestCase(unittest.TestCase):
    def test_average_score(self):
        with mock.patch('builtins.input', side_effect=(-90, 95,85)):
            self.assertRaises(ValueError)



if __name__ == '__main__':
    unittest.main()
