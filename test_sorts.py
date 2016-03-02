import unittest
from SortableList import SortableList

class SortsTestCase(unittest.TestCase):

	# Tests buildOrdered
	def test_build(self):
		test_list = SortableList(100)
		test_list.buildOrdered()
		self.assertTrue(test_list.isSorted())

	# Tests buildReverse
	def test_reverse(self):
		test_list = SortableList(100)
		test_list.buildReverse()
		test_list.my_list.reverse()
		self.assertTrue(test_list.isSorted())

	# Tests Insertion Sort
	def test_insertion(self):
		test_list = SortableList(100)
		test_list.buildRandom()
		test_list.sortInsertion()
		self.assertTrue(test_list.isSorted())

	# Tests built-in sort
	def test_python(self):
		test_list = SortableList(100)
		test_list.buildRandom()
		test_list.sortPython()
		self.assertTrue(test_list.isSorted())

if __name__ == '__main__':
	unittest.main()
