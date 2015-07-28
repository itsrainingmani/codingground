# Hello World program in Python
from SortingAlgo import *
from SearchAlgo import *

def arr_rand(n,m):
    arr = [0 for x in range(n)]
    for num in range(0,n):
        arr[num] = random.randrange(0,m)
    return arr

#bubblesort(10000,10000)
selection_sort(10000,10000)
insertion_sort(10000,10000)
