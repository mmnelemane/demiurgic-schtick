#
# This file contains all of the 100,000 integers between 1 and 100,000 (inclusive)
# in some order, with no integer repeated.
#
# Your task is to compute the number of inversions in the file given, where the
# ith row of the file indicates the ith entry of an array.
#
# Because of the large size of this array, you should implement the fast
# divide-and-conquer algorithm covered in the video lectures.
#
# The numeric answer for the given input file should be typed in the space below.
#
# So if your answer is 1198233847, then just type 1198233847 in the space
# provided without any space / commas / any other punctuation marks.
# You can make up to 5 attempts, and we'll use the best one for grading.
#
# (We do not require you to submit your code, so feel free to use any
# programming language you want --- just type the final numeric answer in
# the following space.)
#
# [TIP: before submitting, first test the correctness of your program on
# some small test files or your own devising. Then post your best test cases
# to the discussion forums to help your fellow students!]
#

# The Algorithm:
# if n=1 return 0
# else
#    (B, x) = sort_and_count(1st half of A, n/2)
#    (C, y) = sort_and_count(2nd half of A, n/2)
#    (D, z) = merge_and_count_split(A, n)
# return x + y + z
#

def sort_and_count_inversions(input1):
    pivot = len(input1)/2
    print "Working with pivot %d" % pivot
    print "Input: ", input1
    if len(input1) == 1:
        return 0
    if len(input1) == 2:
        if (input1[0] > input1[1]):
            return 1
        else:
            return 0
    # inv_count = inv_count + get_split_inversions(input1)
    left_inv = sort_and_count_inversions(input1[:pivot])
    print "Left Inversions: %d" % left_inv
    right_inv = sort_and_count_inversions(input1[pivot:])
    print "Right Inversions: %d" % right_inv
    split_inv = merge_and_count_split_inversions(input1)
    total_env = left_inv + right_inv + split_inv
    return total_env

# Concept for implementing Split Inversions
# The split inversions involving an element Y in 2nd array C are precisely
# the number left in the first array B when Y is copied to the output D.
#
# Proof:
# Let X be an element of the 1st array B
# 1. If X copied to output D before Y, then X < Y +> no inversion
# 2. If Y copied to output D before X, then Y < X => X&Y are split inversions
#

def merge_and_count_split_inversions(input1):
    print "Input in Merge and Split: ", input1
    if len(input1)  == 1:
        return 0
    pivot = len(input1)/2
    print "Working with pivot %d" % pivot
    print "Input: ", input1
    split_inv_count = 0
    sort_left = sorted(input1[:pivot])
    sort_right = sorted(input1[pivot:])
    print "Sorted Left: ", sort_left
    print "Sorted Right: ", sort_right
    rc = 0
    lc = 0
    sort_merge = []
    print "Length of Current Input: %d" % len(input1)
    for i in range(len(input1)):
        print "LC: %d, RC: %d, i: %d" %(lc, rc, i)

        left_element = 99999
        right_element = 99999
        if lc < len(sort_left):
            left_element = sort_left[lc]
        if rc < len(sort_right):
            right_element = sort_right[rc]

        print "Left Element: %d, Right Element: %d" % (left_element, right_element)
        if lc < len(sort_left) and rc < len(sort_right):
            if sort_left[lc] <= sort_right[rc]:
                sort_merge.append(sort_left[lc])
                lc = lc + 1
            elif sort_left[lc] > sort_right[rc]:
                sort_merge.append(sort_right[rc])
                rc = rc + 1
                split_inv_count = split_inv_count + len(sort_left) - lc
            else:
                pass
        print "Sorted Merged: ", sort_merge
        print "Split Inversions: %d" % split_inv_count
    return split_inv_count

def get_input(filename):
    in_list = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            key = int(line.strip('\n'))
            in_list.append(key)
    return in_list


if __name__ == '__main__':
    input_list = get_input('newarray.txt') # [100, 120, 131, 138, 140, 142, 145, 149]
    print "Got Input of Length: %d" % len(input_list)
    inv_count = sort_and_count_inversions(input_list)
    print "Total Inversions in the sequence: %d" % inv_count
