import sys 
sys.path.append(r"")
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """test"""
    formatted_name = get_formatted_name('janis','joplin')
    self.assertEqual(formatted_name,'janis Joplin')


unittest.main()
