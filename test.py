
import time
import sys
import random


before_stamp = time.perf_counter()

def Openfile():

    file = open('/Users/jakobcarlsson/Documents/DV1625 Datastrukturer och algoritmer/Inlämningsuppgift_A/Testdata/1000(0,1000).txt')

    lst = []

    for line in file:
        lst.append(int(line))

    file.close()
    return lst


def Quicksort(lst, l, r):

    # Base case
    if l < r:

        #Call Partition
        i = Partition(lst, l, r)

        #Sorts elements left of pivot
        Quicksort(lst, l, i-1)

        #Sorts elements right of pivot
        Quicksort(lst, i+1, r)


def Partition(lst, l, r):
    # choose pivot
    
    mid = (l + r) // 2
    
    

    if lst[l] < lst[mid] <lst[r]:
        pivot_index = mid
    else:
        pivot_index = l

    # move pivot to first index
    lst[l], lst[pivot_index] = lst[pivot_index], lst[l]

    # partition
    i = l
    for j in range(l+1, r+1):
        if lst[j] < lst[l]:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    
    # place pivot in proper position
    lst[i], lst[l] = lst[l], lst[i]    
    
    return i

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
  
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
  
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
  
        # Heapify the root.
        heapify(arr, n, largest)
  
# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)
  
    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
  
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)


class D_aryHeap:
    def __init__(self, d, items):
            self.items = items
            self.d = d

    def size(self):
        return len(self.items)
    
    def parent(self, i): 
        return (i - 1)//self.d

    def child(self, index, position):
        return index*self.d + (position + 1)

    def get(self, i):
        return self.items[i]

    def get_max(self):
        if self.size() == 0:
            return None 
        return self.items[0]

    def extract_max(self): 
        if self.size() == 0:
            return None
        largest = self.get_max()
        self.items[0] = self.items[-1] 
        del self.items[-1] 
        self.max_heapify(0)
        return largest

    def max_heapify(self, i): 
        largest = i
        for j in range(self.d):
            c = self.child(i, j)
            if (c < self.size() and self.get(c) > self.get(largest)):
                largest = c 
        if (largest != i):
            self.swap(largest, i)
            self.max_heapify(largest)

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def insert(self, key): 
        index = self.size() 
        self.items.append(key) 
        while (index != 0):
            p = self.parent(index)
            if self.get(p) < self.get(index):
                    self.swap(p, index)
            index = p

lst = Openfile()
Quicksort(lst, 0, len(lst)-1)
print(lst)
"""
items = Openfile()

d = 2 
dheap = D_aryHeap(d, items)
print(items)
"""