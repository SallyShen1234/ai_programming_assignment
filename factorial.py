def factorial(n):
    """Calculate the factorial of a number recursively."""
    if n == 0:
        return 1  # Fixed: factorial(0) = 1
    else:
        return n * factorial(n - 1)

print(factorial(5))