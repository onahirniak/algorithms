from os import sys

class ArrayTasks(object):
    
    def max_sub_array(self, arr):
        max_current, max_so_far = 0, -sys.maxsize

        for n in arr:
            max_current += n
            max_so_far = max(max_so_far, max_current)
            max_current = max(0, max_current)
            
        return max_so_far