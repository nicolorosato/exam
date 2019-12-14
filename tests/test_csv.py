import unittest
import sys
from myfolder.test import csv_reader
from myfolder.test import type_file
import os

'''It is necessary to put your personal

path directory to the csv file.
'''
sys.path.append('/Users/nicolorosato/capitals/data/capitals.csv')


class TestMain(unittest.TestCase):

    def setUp(self):
        self.temporary_file = "/tmp/temporary_file.csv"
        f = open(self.temporary_file, 'w')
        f.close()


'''This function is necessary to check

the existence of the csv file.
'''

    def test_no_datafile(self):
        datafile = csv_reader(path=self.temporary_file)
        self.assertIn(".csv", self.temporary_file)

'''This function is necessary to check 

the presence of data inside the csv file.
'''

    def test_empty_datafile(self):
        datafile = csv_reader(path=self.temporary_file)
        self.assertFalse(datafile)

'''This function is necessary to check 

the extension of the file.

'''       
    def test_valid_extension(self):
        extension = type_file(path=self.temporary_file)
        self.assertEqual(extension, ".csv")

    def tearDown(self):
        os.remove(self.temporary_file)

if __name__ == '__main__':
    unittest.main()
