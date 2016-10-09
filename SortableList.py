#!/usr/local/bin/python

# Anton Zipper - CS350 Project - SortableList.py

import sys
from sys import argv    # for command line args
import copy		# for deepcopying lists
import string		# for generating strings
import random		# for putting random numbers in the list
import timeit		# for recording run time
import math		# for log10 function
import csv      # for file output

# A list with various build and sort methods
class SortableList:
    # Constants for parsing input
    BUILD_FEW = "few"
    BUILD_NEARLY = "nearly"
    BUILD_ORDERED = "ordered"
    BUILD_RANDOM = "random"
    BUILD_REVERSE = "reverse"
    BUILD_STRING = "string"
    SORT_BUCKET = "bucket"
    SORT_COCKTAIL = "cocktail"
    SORT_INSERTION = "insertion"
    SORT_MERGE = "merge"
    SORT_PYTHON = "python"
    SORT_QUICK = "quick"
    SORT_SELECTION = "selection"

    def __init__(self, size):
        self.my_list = []
        self.size = size

    def copy(self):
        return copy.deepcopy(self)

    def printList(self):
        print self.my_list

    # Builds the list according to the typ parameter
    def build(self, typ):
        if typ == self.BUILD_FEW:
            self.buildFew()
        elif typ == self.BUILD_NEARLY:
            self.buildNearly()
        elif typ == self.BUILD_ORDERED:
            self.buildOrdered()
        elif typ == self.BUILD_RANDOM:
            self.buildRandom()
        elif typ == self.BUILD_REVERSE:
            self.buildReverse()
        elif typ == self.BUILD_STRING:
            self.buildString()
        else:
            raise Exception("Build not found")

    # Few unique values
    def buildFew(self):
        end = int(math.log10(self.size)) + 1
        for i in range(0, self.size):
            self.my_list.append(random.randrange(0, end))

    # Nearly sorted - swaps 1% of ordered values at random with previous
    def buildNearly(self):
        self.buildOrdered()
        swaps = int(self.size * 0.01) + 1
        end = self.size - 1
        for i in range(0, swaps):
            j = random.randrange(1, end)
            self.my_list[j], self.my_list[j-1] = self.my_list[j-1], self.my_list[j]

    # Ordered - counts up from 0 to size - 1
    def buildOrdered(self):
        for i in range(0, self.size):
            self.my_list.append(i)

    # Random ints between 0 and 99
    def buildRandom(self):
        for i in range(0, self.size):
            self.my_list.append(random.randrange(0, 1000))

    # Reverse - counts down from size - 1
    def buildReverse(self):
        max = self.size - 1
        for i in range(max, -1, -1):
            self.my_list.append(i)

    # String - generates random strings
    def buildString(self):
        for i in range(0, self.size):
            length = random.randrange(3, 10)
            rstring = ''.join([random.choice(string.ascii_lowercase) for j in xrange(length)])
            self.my_list.append(rstring)

    # Checks if self.my_list is sorted
    def isSorted(self):
        for i in range(1, self.size):
            if (self.my_list[i-1] > self.my_list[i]):
                return False
        return True

    # Sorts the list according to the algo parameter
    def sort(self, algo):
        if algo == self.SORT_BUCKET:
            self.sortBucket()
        elif algo == self.SORT_COCKTAIL:
            self.sortCocktail()
        elif algo == self.SORT_INSERTION:
            self.sortInsertion()
        elif algo == self.SORT_MERGE:
            self.sortMerge()
        elif algo == self.SORT_PYTHON:
            self.sortPython()
        elif algo == self.SORT_QUICK:
            self.sortQuick()
        elif algo == self.SORT_SELECTION:
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
        result = []
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

            result += b

        # Point local my_list to sorted list
        self.my_list = result

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
    def merge(sublist):
        # Base case, list of 1 (or empty)
        if len(sublist) < 2:
            return sublist

        # Split list in half and recursively call on each half
        mid = len(sublist) / 2
        right = SortableList.merge(sublist[:mid])
        left = SortableList.merge(sublist[mid:])

        # Combine two halves
        result = []
        r, l = 0, 0
        rlen = len(right)
        llen = len(left)
        while (r < rlen and l < llen):
            # Append current right item if it's smaller
            if right[r] < left[l]:
                result.append(right[r])
                r += 1
            # Otherwise append current left item
            else:
                result.append(left[l])
                l += 1

        # Once either half is done, append the rest
        result += right[r:]
        result += left[l:]

        return result

    # Python sort
    def sortPython(self):
        self.my_list.sort()

    # Quick Sort
    def sortQuick(self):
        self.my_list = SortableList.quick(self.my_list)

    # Quick Sort recursive helper
    @staticmethod
    def quick(sublist):
        # Base case, list of 1 (or empty)
        if len(sublist) < 2:
            return sublist

        # Select random pivot value
        pindex = random.randrange(0,len(sublist))
        pivot = sublist[pindex]

        # Make lists of items less than, greater than, and the same as the pivot
        less, same, greater = [], [], []
        for x in sublist:
            if x < pivot:
                less.append(x)
            elif x > pivot:
                greater.append(x)
            else:
                same.append(x)

        # Sort and return sublists
        less_sorted = SortableList.quick(less)
        greater_sorted = SortableList.quick(greater)
        return less_sorted + same + greater_sorted

    # Selection Sort
    def sortSelection(self):
        for i in range(0,self.size):
            low = i

            # Find the position of the lowest remaining value
            for j in range(i+1,self.size):
                if self.my_list[j] < self.my_list[low]:
                    low = j
            # Swap the ith value with the lowest value
            self.my_list[i], self.my_list[low] = self.my_list[low], self.my_list[i]

# Returns the run time of the chosen sort
def timeSort(to_sort, algo):
    start = timeit.default_timer()
    to_sort.sort(algo)
    stop = timeit.default_timer()
    return (stop - start)

# Runs algo on list, and adds the time it took to the outfile
def outputSort(list, build_type, algo, outfile):
    csv_writer = csv.writer(outfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    time = timeSort(list, algo)
    out_string = algo + " sort: " + str(time)
    print out_string
    # outfile.write('\t' + out_string + '\n')
    csv_writer.writerow([build_type, list.size, algo, time])

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
        with open("output.csv", 'a') as outfile:
            # add heading to file
            # heading = typ + ' ' + str(n) + '\n'
            # outfile.write(heading)

            # Make list and copy it for each sort
            list_buc = SortableList(n)
            list_buc.build(typ)
            list_coc = list_buc.copy()
            list_ins = list_buc.copy()
            list_mrg = list_buc.copy()
            list_py = list_buc.copy()
            list_qck = list_buc.copy()
            list_sel = list_buc.copy()

            # Time how long it takes to run each sort, and output results to the outfile
            if (typ != "string"):
                outputSort(list_buc, typ, SortableList.SORT_BUCKET, outfile)
            outputSort(list_coc, typ, SortableList.SORT_COCKTAIL, outfile)
            outputSort(list_ins, typ, SortableList.SORT_INSERTION, outfile)
            outputSort(list_mrg, typ, SortableList.SORT_MERGE, outfile)
            outputSort(list_py, typ, SortableList.SORT_PYTHON, outfile)
            outputSort(list_qck, typ, SortableList.SORT_QUICK, outfile)
            outputSort(list_sel, typ, SortableList.SORT_SELECTION, outfile)

if __name__ == '__main__':
    main()
