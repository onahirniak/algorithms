from os import sys

class ArrayHelper(object):
    
    def max_sub_array(self, arr):
        max_current, max_so_far = 0, -sys.maxsize

        for n in arr:
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
