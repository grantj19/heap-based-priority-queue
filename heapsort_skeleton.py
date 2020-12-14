#!/usr/bin/python3

import unittest
import math

""" A HeapSort module. For more information on how to implement the functions, refer to 

+ CLRS3, chapter 6: the module's organization follows the text's exposition faithfully.
+ The slides for this course "Heaps: the Owner's Manual": they contain a few useful tips about the Python implementation.

"""

########### DO NOT MODIFY ####################
class HeapCapable(list):
    """
    A HeapCapable object is just a normal Python list, with an extra `heap_size` field. For conveniency, this type is used throughout the module for all arrays, even if they are not actually max-heaps.

    .. warning:: Do not modify this class.
    """
    def __init__(self, lst):
        """
        Initializes a new heap from a list.
        """
        super().__init__(lst) # calling the superclass (list) constructor
        self.heap_size = len(self)


############ ASSIGNMENT STARTS HERE #########

def left(i):
    """
    Return the left child of the given node.
    
    The procedure is just an arithmetical computation of the L child's index. Checking that such a child exists is left to the caller function.

        .. note:: Because Python arrays are numbered from 0 to 1, the pseudo-code shown in CLRS3, chapter 6 needs to be adapted (the slides "Heaps: the Owner's manual" tell you how).
 
    :param i: index of the node in the heap
    :type i: int
    :return: the index of the given node's left child
    :rtype: int
        """
    return (i * 2) + 1

def right(i):
    """
    Return the right child of the given node.

    The procedure is just an arithmetical computation of the R child's index. Checking that such a child exists is left to the caller function.

     .. note:: Because Python arrays are numbered from 0 to 1, the pseudo-code shown in CLRS3, chapter 6 needs to be adapted (the slides "Heaps: the Owner's manual" tell you how).
    
    :param i: index of the node in the heap
    :type i: int
    :return: the index of the given node's right child
    :rtype: int
    """
    return (i * 2) + 2

def parent(i):
    """
    Return the parent of the given node.

    The procedure is just an arithmetical computation of the parent's index. Checking that such a parent exists is left to the caller function.
    
     .. note:: Because Python arrays are numbered from 0 to 1, the pseudo-code shown in CLRS3, chapter 6 needs to be adapted (the slides "Heaps: the Owner's manual" tell you how).

    :param i: index of the node in the heap
    :type i: int
    :return: the index of the given node's parent
    :rtype: int
    """
    return math.floor(((i - 1)/2))

def max_heapify(A,i):
    """
    Given an array A, and assuming that the subtrees rooted at A[i]'s L and R children are max-heaps, restore the max-heap property.

        .. note:: The procedure does not return anything: it simply modifies the array in place.
    
    :param A: an array.
    :param i: the index of the  node to be floated down
    :type A: heapsort_skeleton.HeapCapable
    :type i: int
    """
    l = left(i)
    r = right(i)
    if l <= A.heap_size - 1 and A[l] > A[i]:
        largest = l
    else:
        largest = i
    
    if r <= A.heap_size - 1 and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A,largest)

def build_max_heap(A):
    """ Build a max-heap, from an unsorted array. 
        
        .. note:: The procedure does not return anything: it modifies the array in place.

    :param A: the array to be sorted.
    :type A: heapsort_skeleton.HeapCapable
    """
    A.heap_size = len(A)

    for i in range((len(A)), -1, -1):
        max_heapify(A,i)

def heap_max(A):
    return A[0]

def heap_extract_max(A):
    if A.heap_size < 1:
        #throw heap underflow
        raise ValueError("Heap Underflow")
    max = A[0]
    A[0] = A[A.heap_size - 1]
    A.heap_size = A.heap_size - 1
    max_heapify(A, 0)
    return max

def heap_increase_key(A,i,key):
    if key < A[i]:
        raise ValueError("New key is smaller than current value")
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)

def max_heap_insert(A, key):
    A.heap_size = A.heap_size + 1
    A.append(-1)
    heap_increase_key(A, A.heap_size - 1, key)



def HeapSort(A):
    """ Sort the array in place.
    
    .. note:: The function sorts in place, and therefore does not return anything.

    :param A: an array, with values in random order - do not assume that the array is already a max-heap! The `build_max_heap` procedure needs to be run on A before the actual sorting takes place.
    :type A: heapsort_skeleton.HeapCapable
    """
    build_max_heap(A)

    for i in range(len(A)-1, -1, -1):
        A[0], A[i] = A[i], A[0]

        A.heap_size = A.heap_size - 1

        max_heapify(A,0)




############# DO NOT MODIFY ##############################
class testHeapSort(unittest.TestCase):

    
    def test_left_1(self):
        self.assertEqual( left(0), 1 )

    def test_left_2(self):
        self.assertEqual( left(2), 5 )

    def test_left_3(self):
        self.assertEqual( left(3), 7 )

    def test_right_1(self):
        self.assertEqual( right(0), 2 )

    def test_right_2(self):
        self.assertEqual( right(2), 6 )

    def test_right_3(self):
        self.assertEqual( right(3), 8 )

    def test_parent_1(self):
        self.assertEqual( parent(1), 0 )
    
    def test_parent_2(self):
        self.assertEqual( parent(2), 0 )
    
    def test_parent_3(self):
        self.assertEqual( parent(3), 1 )
    
    def test_parent_4(self):
        self.assertEqual( parent(4), 1 )

    def test_max_heapify_general_case(self):
        """ 
        CLRS3, exercise 6.2-1
        """
        A = HeapCapable([ 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0 ])
        max_heapify(A,2)
        self.assertEqual( A, [27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0])

    def test_max_heapify_untouched(self):
        """ 
        MaxHeapify() does not change the array if A[i] is larger than its two children
        """
        A = HeapCapable([ 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0 ])
        max_heapify(A, 1)
        self.assertEqual(A, [ 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0 ])


    def test_max_heapify_reduced_heap_size(self):
        """ 
        Max-Heapify() should always ckeck against the heap's size, not the array's length!
        """
        A = HeapCapable([ 3, 10, 7, 9, 7, 5, 2, 8, 5, 4 ])
        A.heap_size=7
        max_heapify(A,0)
        self.assertEqual( A, [ 10, 9, 7, 3, 7, 5, 2, 8, 5, 4 ])


    def test_buildmaxheap_unique_values(self):
        """
        BuildMaxHeap: general case, with non-repeated values
        """
        A = HeapCapable([19, 5, 3, 16, 8, 2, 18, 13, 1, 17, 10, 4, 6, 12])
        build_max_heap(A)
        self.assertEqual(A, [19, 17, 18, 16, 10, 6, 12, 13, 1, 8, 5, 4, 2, 3])

    def test_buildmaxheap_repeated_values(self):
        """
        BuildMaxHeap: general case, with repeated values
        """
        A = HeapCapable([7, 16, 7, 4, 8, 13, 18, 3, 10, 7, 12, 8, 17, 3])
        build_max_heap(A)
        self.assertEqual(A, [18, 16, 17, 10, 12, 13, 7, 3, 4, 7, 8, 8, 7, 3])

    def test_buildmaxheap_1_element_array(self):
        """
        BuildMaxHeap: special case - 1-element array
        """
        A = HeapCapable([7])
        build_max_heap(A)
        self.assertEqual(A, [7])

    def test_heapsort_unique_values(self):
        """
        HeapSort: general case, with unique values
        """
        A = HeapCapable([19, 5, 3, 16, 8, 2, 18, 13, 1, 17, 10, 4, 6, 12])
        HeapSort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5, 6, 8, 10, 12, 13, 16, 17, 18, 19])

    def test_heapsort_repeated_values(self):
        """
        HeapSort: general case, with repeated values
        """
        A = HeapCapable([7, 16, 7, 4, 8, 13, 18, 3, 10, 7, 12, 8, 17, 3])
        HeapSort(A)
        self.assertEqual(A, [3, 3, 4, 7, 7, 7, 8, 8, 10, 12, 13, 16, 17, 18])

    def test_heapsort_1_element_array(self):
        """
        HeapSort: special case - 1-element array
        """
        A = HeapCapable([7])
        HeapSort(A)
        self.assertEqual(A, [7])

    def test_heap_max(self):
        A = HeapCapable([7, 16, 7, 4, 8, 13, 18, 3, 10, 7, 12, 8, 17, 3])
        max = heap_max(A)
        self.assertEqual(max, A[0])

    def test_heap_extract_max(self):
        A = HeapCapable([ 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0 ])
        extracted_max = heap_extract_max(A)
        self.assertEqual(extracted_max, 27)

    #Add this later
    def test_heap_increase_key(self):
        A = HeapCapable([17, 16, 3, 7, 13, 10, 1, 5, 0, 12, 4, 8, 9, 0])
        heap_increase_key(A, 8, 20)
        self.assertEqual(A, [20, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0])

    def test_heap_insert_key(self):
        A = HeapCapable([17, 16, 3, 7, 13, 10, 1, 5, 0, 12, 4, 8, 9, 0])
        max_heap_insert(A, 15)
        self.assertEqual(A, [17, 16, 15, 7, 13, 10, 3, 5, 0, 12, 4, 8, 9, 0, 1])

    def test_heap_insert_key_max(self):
        A = HeapCapable([17, 16, 3, 7, 13, 10, 1, 5, 0, 12, 4, 8, 9, 0])
        max_heap_insert(A, 24)
        self.assertEqual(A, [24, 16, 17, 7, 13, 10, 3, 5, 0, 12, 4, 8, 9, 0, 1])






def main():
        unittest.main()

if __name__ == '__main__':
        main()


