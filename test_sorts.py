import unittest
from SortableList import SortableList

class SortsTestCase(unittest.TestCase):

	def test_insertion(self):
		my_list = SortableList(100)
		my_list.buildRandom()
		my_list.sortInsertion()
		self.assertTrue(my_list.isSorted())

if __name__ == '__main__':
	unittest.main()
