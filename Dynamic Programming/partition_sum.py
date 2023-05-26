def main():
    array = [1, 5, 1, 5, 7, 3, 6, 1, 8, 9, 3]
    k = 4
    n = len(array)
    sums = [0 for _ in range(n)] # Initializing an array of length N (All 0's)
    for i in range(n):
        # Base case if we chose to include a subset of 1
        prev_value = 0
        if i > 0:
            prev_value = sums[i - 1]
        sums[i] = array[i] + prev_value
        
        # Check the value for all other subset sizes
        # Don't go past the end of the list
        temp = array[i]
        for j in range(1, min(k, i) + 1):
            temp = max(temp, array[i - j])
            sums[i] = max(sums[i], temp * j + sums[i-j])
    print(sums[n-1])

main()