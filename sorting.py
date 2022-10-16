import time

def Openfile():

    file = open('Inlämningsuppgift_A/Testdata/sorted_reverse_100000.txt')

    lst = []

    for line in file:
        lst.append(int(line))

    file.close()
    return lst

def quicksort_pivot_first(lst, first=None, last=None):
    """Quicksort algoritm med första elementet som partitioneringselement."""
    if first is None:
        first = 0
    if last is None:
        last = len(lst)-1
    if last > first:   
        index = partition_first(lst, first, last) 
        quicksort_pivot_first(lst, first, index-1)
        quicksort_pivot_first(lst, index+1, last)

def partition_first(lst, first, last):
    """Partitionering"""
    pivot_index = first
    lst[first], lst[pivot_index] = lst[pivot_index], lst[first]
    index = first
    for j in range(first+1, last+1):
        if lst[j] < lst[first]:
            index += 1
            lst[index], lst[j] = lst[j], lst[index]
    lst[index], lst[first] = lst[first], lst[index]
    return index

def quicksort_pivot_median(lst, first = None, last = None):
    """Quicksort algorithm med medinaen av tre(first, mitt, slut) som partitioneringselement."""
    if first is None:
        first = 0
    if last is None:
        last = len(lst)-1
    if first < last: 
        index = partition_median(lst, first, last)
        quicksort_pivot_median(lst, first, index-1)
        quicksort_pivot_median(lst, index+1, last)

def partition_median(lst, first, last):
    """Partitionering"""
    mid = (first + last) // 2
    pivot_index = first
    if lst[first] < lst[mid] < lst[last]:
        pivot_index = mid
    elif lst[first]<lst[last]<lst[mid]:
        pivot_index = first
    elif lst[mid]<lst[first]<lst[last]:
        pivot_index = first
    elif lst[mid]<lst[last]<lst[first]:
        pivot_index = last
    elif lst[last]<lst[mid]<lst[first]:
        pivot_index = mid
    elif lst[last]<lst[first]<lst[mid]:
        pivot_index = first
    lst[first], lst[pivot_index] = lst[pivot_index], lst[first]
    index = first
    for j in range(first+1, last+1):
        if lst[j] < lst[first]:
            index += 1
            lst[index], lst[j] = lst[j], lst[index]
    lst[index], lst[first] = lst[first], lst[index] 
    return index

def heapsort(array, leafs=2):
    """The heapsort algorithm"""
    length = len(array)
    build_max_heap(array, leafs)
    for index in range(length - 1, 0, -1):
        array[index], array[0] = array[0], array[index]
        max_heapify(array, index, 0, leafs)

def get_child(index, j, leafs: int):
    """Finds the children"""
    child = int(leafs * index + (j + 1))
    return child

def max_heapify(array, length, parent_index, leafs):
    """Heapify"""
    largest = parent_index
    for j in range(leafs+1):
        childi = get_child(parent_index, j, leafs)
        if childi < length and array[childi] > array[largest]:
            largest = childi
    if largest != parent_index:
        array[parent_index], array[largest] = array[largest], array[parent_index]
        max_heapify(array, length, largest, leafs)

def build_max_heap(array, leafs):
    """Building maxheap"""
    length = len(array)
    for index in range(length //leafs, -1, -1):
        max_heapify(array, length, index, leafs)

lst = Openfile()
before_stamp = time.perf_counter()
heapsort(lst, 4)
after_stamp = time.perf_counter()
time = float(after_stamp-before_stamp)
print("Time: ", time)
