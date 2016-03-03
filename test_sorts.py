import unittest
from SortableList import SortableList

class SortsTestCase(unittest.TestCase):

	# buildOrdered test
	def test_build(self):
		test_list = SortableList(100)
		test_list.buildOrdered()
		self.assertTrue(test_list.isSorted())

	# buildReverse test
	def test_reverse(self):
		test_list = SortableList(100)
		test_list.buildReverse()
		test_list.my_list.reverse()
		self.assertTrue(test_list.isSorted())

	# Bucket Sort test
	def test_bucket(self):
		test_list = SortableList(100)
		test_list.buildRandom()
		test_list.sortBucket()
		self.assertTrue(test_list.isSorted())

	# Cocktail Sort test
	def test_cocktail(self):
		test_list = SortableList(100)
		test_list.buildRandom()
		test_list.sortCocktail()
		self.assertTrue(test_list.isSorted())

	# Insertion Sort test
	def test_insertion(self):
		test_list = SortableList(100)
		test_list.buildRandom()
		test_list.sortInsertion()
		self.assertTrue(test_list.isSorted())

	# Merge Sort test
	def test_merge(self):
		test_list = SortableList(100)
		test_list.buildRandom()
		test_list.sortMerge()
		self.assertTrue(test_list.isSorted())

	# Python built-in sort test
	def test_python(self):
		test_list = SortableList(100)
		test_list.buildRandom()
		test_list.sortPython()
		self.assertTrue(test_list.isSorted())

	# Quick Sort test
	def test_quick(self):
		test_list = SortableList(100)
		test_list.buildRandom()
		test_list.sortQuick()
		self.assertTrue(test_list.isSorted())

if __name__ == '__main__':
	unittest.main()
