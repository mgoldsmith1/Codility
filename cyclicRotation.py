import unittest
import random


'''
An array A consisting of N integers is given. 
Rotation of the array means that each element is shifted right by one index, 
and the last element of the array is moved to the first place. 
For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] 
(elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be 
shifted to the right K times.

Write a function:

def solution(A, K)

that, given an array A consisting of N integers and an integer K, 
returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
In your solution, focus on correctness. The performance of your solution 
will not be the focus of the assessment.
'''

def solution(A, K):
    # write your code in Python 3.6

    if len(A) == 0 or len(A) == 1:
        return A
    
    n = len(A) - 1
    
    i = n
    B = A
    j = n
    idx = 0
    endVal = B[n]
    startVal = B[0]

    while idx < K:
        while i > 1:
            B[j] = A[i-1]
            i -= 1
            j -= 1
        B[0] = endVal
        B[1] = startVal
        endVal = B[n]
        startVal = B[0]
        i = n
        j = n
        idx += 1
        
    return B
    
class TestSkeleton(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(solution([], 0), [])
        
    def test_zeros_array(self):
        self.assertEqual(solution([0, 0, 0], 1), [0, 0, 0])
    
    def test_solution(self):
        self.assertEqual(solution([3,8,9,7,6], 1),[6,3,8,9,7])

    def test_three(self):
        self.assertEqual(solution([3,8,9,7,6], 3), [9,7,6,3,8])
    
    def test_reflexive(self):
        self.assertEqual(solution([1,2,3,4], 4), [1,2,3,4])

    


if __name__ == '__main__':
    unittest.main()
