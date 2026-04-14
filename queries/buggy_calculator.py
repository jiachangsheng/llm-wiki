"""
Simple Calculator with a bug.
Can you find it?
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Bug here - but what's the root cause?
    if b != 0:
        return a / b
    return 0

def calculate_average(numbers):
    """Calculate average of a list of numbers."""
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    
    # Hint: The bug is related to this function's behavior
    return divide(total, count)

def calculate_sum(numbers):
    """Calculate sum of all numbers."""
    result = 0
    for num in numbers:
        result += num
    return result

if __name__ == "__main__":
    # Test cases
    print(f"Add: 2 + 3 = {add(2, 3)}")
    print(f"Multiply: 4 * 5 = {multiply(4, 5)}")
    print(f"Average: [1, 2, 3, 4, 5] = {calculate_average([1, 2, 3, 4, 5])}")
    print(f"Sum: [10, 20, 30] = {calculate_sum([10, 20, 30])}")
