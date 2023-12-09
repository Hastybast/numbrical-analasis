def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    """
    Bisection method to find the root of a function.

    Parameters:
    - func: The target function.
    - a, b: The interval [a, b] where the root is expected.
    - tol: Tolerance, the acceptable error in the result.
    - max_iter: Maximum number of iterations.

    Returns:
    - root: Approximation of the root.
    - iterations: Number of iterations performed.
    """

    # Check if the interval is valid (different signs at the endpoints)
    if func(a) * func(b) > 0:
        raise ValueError("The function values at the endpoints must have different signs.")

    # Initialize variables
    iteration = 0

    while (b - a) / 2 > tol and iteration < max_iter:
        c = (a + b) / 2  # Midpoint

        if func(c) == 0:
            # Found the exact root
            return c, iteration

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

        iteration += 1

    # Return the midpoint of the final interval as the root approximation
    root = (a + b) / 2
    return root, iteration


# Example usage:
if __name__ == "__main__":
    # Define the target function
    def target_function(x):
        return x**3 - x**2 - 1

    # Define the interval [a, b] where the root is expected
    a, b = 1, 2

    # Call the bisection method
    root, iterations = bisection_method(target_function, a, b)

    # Print the result
    print(f"Approximate root: {root}")
    print(f"Iterations performed: {iterations}")