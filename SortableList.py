#!/usr/local/bin/python

# Anton Zipper - CS350 Project - SortableList.py

import sys
from sys import argv	# for command line args
import copy		# for deepcopying lists
import string		# for generating strings
import random		# for putting random numbers in the list
import timeit		# for recording run time

# A list with various build and sort methods
class SortableList:

	def __init__(self, size):
		self.my_list = []
		self.size = size

	def copy(self):
		return copy.deepcopy(self)

	def printList(self):
		print self.my_list

	# Builds the list according to the typ parameter
	def build(self, typ):
		if (typ == "few"):
			self.buildFew()
		elif (typ == "nearly"):
			self.buildNearly()
		elif (typ == "ordered"):
			self.buildOrdered()
		elif (typ == "random"):
			self.buildRandom()
		elif (typ == "reverse"):
			self.buildReverse()
		elif (typ == "string"):
			self.buildString()
		else:
			raise Exception("Build not found")

	# Few unique values
	def buildFew(self):
		mod = int(self.size * 0.01) + 2
		for i in range(0,self.size):
			rand = random.randrange(0,100)
			num = rand % mod
			self.my_list.append(num)

	# Nearly sorted - swaps 1% of ordered values at random with previous
	def buildNearly(self):
		self.buildOrdered()
		swaps = int(self.size * 0.01) + 1
		end = self.size - 1
		for i in range(0,swaps):
			j = random.randrange(1,end)
			self.my_list[j], self.my_list[j-1] = self.my_list[j-1], self.my_list[j]

	# Ordered - counts up from 0
	def buildOrdered(self):
		for i in range(0,self.size):
			self.my_list.append(i)

	# Random ints between 0 and 99
	def buildRandom(self):
		for i in range(0,self.size):
			self.my_list.append(random.randrange(0,100))

	# Reverse - counts down from size - 1
	def buildReverse(self):
		max = self.size -1
		for i in range(max, -1, -1):
			self.my_list.append(i)

	# String - generates random strings
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

	# Sorts the list according to the algo parameter
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
		elif (algo == "shell"):
			self.sortShell()
		else:
			raise Exception("Sort not found")

	# TODO
	# Bucket Sort
	def sortBucket(self):
		print "Not yet implemented"

	# Insertion Sort
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

	# TODO
	# Merge Sort
	def sortMerge(self):
		print "Not yet implemented"

	# Python sort
	def sortPython(self):
		self.my_list.sort()

	# TODO
	# Quick Sort
	def sortQuick(self):
		print "Not yet implemented"

	# TODO
	# Selection Sort
	def sortSelection(self):
		print "Not yet implemented"

	# TODO
	# Shell sort
	def sortShell(self):
		print "Not yet implemented"

# Returns the run time of the chosen sort
def timeSort(to_sort, algo):
	start = timeit.default_timer()
	to_sort.sort(algo)
	stop = timeit.default_timer()
	return (stop - start)

def main():
	# Get command line args for other runs... 
	if (len(argv) >= 4):
		script, algo, typ, n = argv
		n = int(n)
	# ... or prompt the user if there are no args
	else:
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
		with open("output.txt", 'a') as outfile:
			# add heading to file
			heading = typ + ' ' + str(n) + '\n'
			outfile.write(heading)

			# Make list and copy it for each sort
			list_ins = SortableList(n)
			list_ins.build(typ)
			list_py = list_ins.copy()

			# Run and time insertion sort
			time_ins = timeSort(list_ins, 'insertion')
			string_ins = "Insertion sort: " + str(time_ins)
			print string_ins
			outfile.write('\t' + string_ins + '\n')

			# Run and time built-in python sort
			time_py = timeSort(list_py, 'python')
			string_py = "Python sort: " + str(time_py)
			print string_py
			outfile.write('\t' + string_py + '\n')

if __name__ == '__main__':
	main()
