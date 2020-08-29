class Sorter:
    
    def selection_sort(self, arr):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[i]:
                    arr[j], arr[i] = arr[i], arr[j]

    def bubble_sort(self, arr):
        for i in range(len(arr)):
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j] 

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):

            j = i - 1

            while j >= 0 and arr[i] < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = arr[i]

    def quicksort(self, seq):
        if len(seq) <= 1: return seq
        lo, pi, hi = self.partition(seq)
        return self.quicksort(lo) + [pi] + self.quicksort(hi)

    def partition(self, seq):
        pi, seq = seq[0], seq[1:]
        lo = [x for x in seq if x <= pi]
        hi = [x for x in seq if x > pi]
        return lo, pi, hi