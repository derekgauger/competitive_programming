import time

def merge_sort(array):
    if len(array) < 2:
        return
    
    # Divide the array into two equal(ish) sized pieces
    mid = int(len(array) / 2)
    left = [0 for _ in range(mid)] # Initialize an array of length mid (All 0's)
    right = [0 for _ in range(len(array) - mid)] # Intitialize an array of length N - mid (All 0's)

    for i in range(mid):
        left[i] = array[i]

    for i in range(mid, len(array)):
        right[i - mid] = array[i]
    
    # Merge sort each half
    merge_sort(left)
    merge_sort(right)
    # Merge the two back together
    merge(array, left, right)


def merge(array, left, right):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        # Left smaller than right?
        # Add the left element to the array
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        # Right smaller than left?
        # Add the right element to the array
        else:
            array[k] = right[j]
            j += 1
        k += 1
    
    # Copy the leftover elements
    while i < len(left):
        array[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        array[k] = right[j]
        k += 1
        j += 1


def main():
    n = 100
    array = [i + 1 for i in reversed(range(n))]
    print(array)
    start = time.perf_counter_ns()
    merge_sort(array)
    end = time.perf_counter_ns()
    print(array)
    print("Runtime (ns): {}".format(end - start))
  
main()