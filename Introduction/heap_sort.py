import time

def heap_sort(array):
    # Build heap (rearrange array)
    # This for loop is starting at (N / 2 - 1) and iterating through 0
    for i in reversed(range(int(len(array) / 2 - 1))):
        heapify(array, len(array), i)
    
    # One by one extract an element from the heap
    for i in reversed(range(len(array))):
        # Move current root to end
        temp = array[0]
        array[0] = array[i]
        array[i] = temp
        # Call max heapify on the reduced heap
        heapify(array, i, 0)


def heapify(array, n, i):
    # Find largest among root, left child and right child
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    # Swap and continue heapifying if root is not largest
    if largest != i:
        temp = array[largest]
        array[largest] = array[i]
        array[i] = temp
        heapify(array, n, largest)


def main():
    n = 100
    array = [i + 1 for i in reversed(range(n))]
    print(array)
    start = time.perf_counter_ns()
    heap_sort(array)
    end = time.perf_counter_ns()
    print(array)
    print("Runtime (ns): {}".format(end - start ))

main()