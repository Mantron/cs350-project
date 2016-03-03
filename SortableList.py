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
		elif (algo == "cocktail"):
			self.sortCocktail()
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

	# Bucket Sort
	# Doesn't work with strings
	def sortBucket(self):
		# Find highest value to figure out number of buckets
		high = 0
		for x in self.my_list:
			if (x > high):
				high = x
		r = high / 10 + 1
		buckets = [[] for x in range(r)]

		# Distribute the elements of your list into buckets
		for x in self.my_list:
			buckets[int(x/10)].append(x)

		# Sort and join each bucket
		out = []
		for b in buckets:
			# Insertion Sort
			blen = len(b)
			for i in range(1, blen):
				current = b[i]
				j = i - 1
				while ((j >= 0) and (b[j] > current)):
					b[j+1] = b[j]
					j -= 1
				b[j+1] = current

			out += b
		self.my_list = out

	# Cocktail Sort
	def sortCocktail(self):
		start = -1
		end = self.size - 2
		swapped = True
		
		# List is sorted when you make it through the list with no swaps
		while swapped:
			# Forward pass
			swapped = False
			for i in range(start+1, end):
				if self.my_list[i] > self.my_list[i+1]:
					self.my_list[i], self.my_list[i+1] = self.my_list[i+1], self.my_list[i]
					swapped = True
			if not swapped:
				break
			# Backward pass
			swapped = False
			for i in range(end, start, -1):
				if self.my_list[i] > self.my_list[i+1]:
					self.my_list[i], self.my_list[i+1] = self.my_list[i+1], self.my_list[i]
					swapped = True

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

	# Merge Sort
	def sortMerge(self):
		self.my_list = SortableList.merge(self.my_list)

	# Merge Sort recursive helper
	@staticmethod
	def merge(items):
		result = []

		# Base case
		if len(items) < 2:
			return items

		# Split list in half and recursively call on each half
		mid = len(items) / 2
		right = SortableList.merge(items[:mid])
		left = SortableList.merge(items[mid:])

		# Combine two halves
		r = 0
		l = 0
		while (r < len(right) and l < len(left)):
			if right[r] > left[l]:
				result.append(left[l])
				l += 1
			else:
				result.append(right[r])
				r += 1

		# Once either half is done, append the rest of the other half
		result += right[r:]
		result += left[l:]

		return result

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
			list_buc = SortableList(n)
			list_buc.build(typ)
			list_coc = list_buc.copy()
			list_ins = list_buc.copy()
			list_mrg = list_buc.copy()
			list_py = list_buc.copy()

			# Run and time bucket sort
			if (typ != "string"):
				time_buc = timeSort(list_buc, 'bucket')
				string_buc = "Bucket sort: " + str(time_buc)
				print string_buc
				outfile.write('\t' + string_buc + '\n')

			# Run and time cocktail sort
			time_coc = timeSort(list_coc, 'cocktail')
			string_coc = "Cocktail sort: " + str(time_coc)
			print string_coc
			outfile.write('\t' + string_coc + '\n')

			# Run and time insertion sort
			time_ins = timeSort(list_ins, 'insertion')
			string_ins = "Insertion sort: " + str(time_ins)
			print string_ins
			outfile.write('\t' + string_ins + '\n')

			# Run and time merge sort
			time_mrg = timeSort(list_mrg, 'merge')
			string_mrg = "Merge sort: " + str(time_mrg)
			print string_mrg
			outfile.write('\t' + string_mrg + '\n')

			# Run and time python built-in sort
			time_py = timeSort(list_py, 'python')
			string_py = "Python sort: " + str(time_py)
			print string_py
			outfile.write('\t' + string_py + '\n')

if __name__ == '__main__':
	main()
