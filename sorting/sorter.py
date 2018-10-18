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