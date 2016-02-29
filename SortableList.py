#!/usr/local/bin/python

# Anton Zipper - CS350 Project - SortableList.py

import sys
from sys import argv
import copy
import string
import random
import timeit

class SortableList:

	def __init__(self, size):
		self.my_list = []
		self.size = size

	def copy(self):
		return copy.deepcopy(self)

	def printList(self):
		print self.my_list

	def build(self, typ):
		if (typ == "ordered"):
			self.buildOrdered()
		elif (typ == "random"):
			self.buildRandom()
		elif (typ == "reverse"):
			self.buildReverse()
		elif (typ == "string"):
			self.buildString()
		else:
			raise Exception("Build not found")

	def buildOrdered(self):
		for i in range(0,self.size):
			self.my_list.append(i)

	def buildRandom(self):
		for i in range(0,self.size):
			self.my_list.append(random.randrange(0,100))

	def buildReverse(self):
		max = self.size -1
		for i in range(max, -1, -1):
			self.my_list.append(i)

	def buildString(self):
		for i in range(0, self.size):
			length = random.randrange(3,10)
			rstring = ''.join([random.choice(string.ascii_lowercase) for j in xrange(length)])
			self.my_list.append(rstring)		

	# Checks if self.my_list is sorted
	def isSorted(self):
		for i in range(1, self.size):
			if (self.my_list[i-1] > self.my_list[i]):
				return false
		return True

	def sort(self, algo):
		if (algo == "bucket"):
			self.sortBucket()
		elif (algo == "insertion"):
			self.sortInsertion()
		elif (algo == "merge"):
			self.sortMerge()
		elif (algo == "python"):
			self.sortPython()
		elif (algo == "quick"):
			self.sortQuick()
		elif (algo == "selection"):
			self.sortSelection()
		else:
			raise Exception("Sort not found")

	def sortBucket(self):
		print "Not yet implemented"

	def sortInsertion(self):

		# For each element in the list...
		for i in range(1, self.size):
			current = self.my_list[i]
			j = i - 1

			# ... look at every element before it
			# and shift up every element while they're greater
			# stop when you find a value smaller than current
			while ((j >= 0) and (self.my_list[j] > current)):
				self.my_list[j+1] = self.my_list[j]
				j -= 1

			# insert current after the smaller value
			self.my_list[j+1] = current

	def sortMerge(self):
		print "Not yet implemented"

	def sortPython(self):
		self.my_list.sort()

	def sortQuick(self):
		print "Not yet implemented"

	def sortSelection(self):
		print "Not yet implemented"

def timeSort(to_sort, algo):
	start = timeit.default_timer()
	to_sort.sort(algo)
	stop = timeit.default_timer()
	return (stop - start)

def main():
	if (len(argv) >= 4):
		script, algo, typ, n = argv
		n = int(n)
	else:
		script = argv[0]	
		algo = raw_input("Which sort? ")
		typ = raw_input("How to build? ")
		n = int(raw_input("How many elements? "))
	
	# Run one sort
	if (algo != 'all'):
		# Make list 
		list1 = SortableList(n)
		list1.build(typ)

		# Print original list
		print "Orignal list: "
		list1.printList()

		# Sort original list and time the sort
		time = timeSort(list1, algo)

		# Printed sorted list with run time
		print "Sorted list: "
		list1.printList()
		print "Running time: " + str(time)

	# Run all sorts
	elif (algo == 'all'):
		# Make list and copies
		list_ins = SortableList(n)
		list_ins.build(typ)
		list_py = list_ins.copy()

		# Run and time insertion sort
		time_ins = timeSort(list_ins, 'insertion')
		print "Insertion sort: " + str(time_ins)

		# Run and time built in python sort
		time_py = timeSort(list_py, 'python')
		print "Python sort: " + str(time_py)

if __name__ == '__main__':
	main()
