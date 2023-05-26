import time

def fib_recursive(n):
    if n == 0 or n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def get_fib_recursive(count):
    result = []
    for i in range(count):
        result.append(fib_recursive(i))
    return result

def fib_iterative(n):
    prev_value = 1
    prev_prev_value = 0
    curr_value = 1
    for i in range(n):
        curr_value = prev_value + prev_prev_value
        prev_prev_value = prev_value
        prev_value = curr_value
    return curr_value

def get_fib_iterative(count):
    result = []
    for i in range(count):
        result.append(fib_iterative(i))
    return result

def get_fib_dp(count):
    result = []
    for i in range(count):
        if i == 0 or i == 1:
            result.append(1)
        else:
            result.append(result[i - 1] + result[i - 2])
    return result

def main():
    count = 20
    # Recursive Fib
    start = time.perf_counter_ns()
    result = get_fib_recursive(count)
    end = time.perf_counter_ns()
    print(result)
    print("Runtime (ns): {}".format(end - start))
    # Iterative Fib
    start = time.perf_counter_ns()
    result = get_fib_iterative(count)
    end = time.perf_counter_ns()
    print(result)
    print("Runtime (ns): {}".format(end - start))
    # Dynamic Programming Fib
    start = time.perf_counter_ns()
    result = get_fib_dp(count)
    end = time.perf_counter_ns()
    print(result)
    print("Runtime (ns): {}".format(end - start))


main()

# Standard Fib: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]