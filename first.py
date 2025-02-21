import numpy as np

def solve_polynomial(coefficients):
    roots = np.roots(coefficients)
    return roots

def main():
    print("Polynomial Solver")
    coefficients = list(map(float, input("Enter polynomial coefficients (highest degree first, space-separated): ").split()))
    roots = solve_polynomial(coefficients)
    print("Roots of the polynomial:", roots)

if __name__ == "__main__":
    main()
