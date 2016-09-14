# cs350-project
A Python script that runs a variety of sorting algorithms on different types of
lists, and displays the running times for each. You may select an individual
sort to time, or run them all. When all sorts are chosen, the results are
logged to the file "output.txt", in addition to being displayed on the screen.

## Usage
$python SortableList.py "sort type" "list type" "number of elements"

ex.

    $python SortableList.py all random 100

Sort types:
 * all
 * bucket
 * cocktail
 * insertion
 * merge
 * python
 * quick
 * selection

List types:
 * few - few unique ints
 * nearly - nearly sorted list of ints
 * ordered - ints counting up from 0 to n
 * random - random ints
 * reverse - ints counting down from n-1 to 0
 * string - randomly generated strings
