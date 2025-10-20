import unittest
from src.ecom_analysis.data_loader import load_data

class TestDataLoader(unittest.TestCase):

    def test_load_csv(self):
        # Test loading a CSV file
        data = load_data('data/raw/sample_data.csv')
        self.assertIsNotNone(data)
        self.assertTrue(len(data) > 0)

    def test_load_invalid_file(self):
        # Test loading an invalid file
        with self.assertRaises(FileNotFoundError):
            load_data('data/raw/non_existent_file.csv')

if __name__ == '__main__':
    unittest.main()