from os import sys

class ArrayHelper(object):
    
    """
    Maximum sub-array problem
    https://en.wikipedia.org/wiki/Maximum_subarray_problem
    """
    def max_sub_array(self, arr):

        if not arr:
            return None

        max_current = max_so_far = arr[0]

        for n in arr[1:]:
            max_current += n
            max_so_far = max(max_so_far, max_current)
            max_current = max(0, max_current)
            
        return max_so_far

    def binary_search(self, arr, val):
        l,r = 0, len(arr) - 1

        while l <= r:
            mid = (l+r) // 2

            if arr[mid] == val:
                return mid

            if arr[mid] > val:
                r = mid - 1
            else:
                l = mid + 1
            
        return -1
