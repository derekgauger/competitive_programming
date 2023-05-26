import time

def sum(n):
    if (n == 1):
        return 1
    return n + sum(n - 1)

def main():
    n = 10
    start = time.perf_counter_ns()
    result = sum(n)
    end = time.perf_counter_ns()

    print("{} : {}".format(n, result))
    print("Runtime (ns): {}".format(end - start))

main()