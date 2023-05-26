class Combinations():
    def __init__(self, n, k):
        self.n = n 
        self.k = k
        self.values = [0 for _ in range(k)]
        self.result = []

    def solve(self, i, j):
        if j == self.k:
            # Reached the limit to 'k' add elements to the result
            list = [i for i in self.values]
            self.result.append(list) 
        else:
            # Build up the potential values in the subset
            self.values[j] = i
            # Solve for the next larger n and k
            self.solve(i + 1, j + 1)
            # If current 'n' is larger than current 'k'
            # solve for the next size larger 'n'
            if self.n - i >= self.k - j:
                self.solve(i + 1, j)

def main():
    solver = Combinations(4, 2)
    # Starting case
    solver.solve(1, 0)
    print(solver.result)
    
main()