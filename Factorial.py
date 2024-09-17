def factorial(X):
    # Handle the case for negative integers
    if X < 0:
        return -1
    
    # Base case: factorial of 0 or 1 is 1
    if X == 0 or X == 1:
        return 1
    
    # Recursive case: X * factorial(X - 1)
    return X * factorial(X - 1)

# Example usage:
result = factorial(5)
print(result)  # Output will be 120

negative_result = factorial(-5)
print(negative_result)  # Output will be -1
