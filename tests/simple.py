"""
Simple test module with sample code for testing purposes.
"""
from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Add two numbers and return the result."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Expected numeric types, got {type(a).__name__} and {type(b).__name__}")
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Subtract b from a and return the result."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Expected numeric types, got {type(a).__name__} and {type(b).__name__}")
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers and return the result."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Expected numeric types, got {type(a).__name__} and {type(b).__name__}")
    return a * b


def divide(a: Number, b: Number) -> float:
    """Divide a by b and return the result."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Expected numeric types, got {type(a).__name__} and {type(b).__name__}")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class Calculator:
    """A simple calculator class."""

    def __init__(self):
        self.result = 0

    def add(self, value):
        """Add value to result."""
        self.result += value
        return self.result

    def subtract(self, value):
        """Subtract value from result."""
        self.result -= value
        return self.result

    def reset(self):
        """Reset result to zero."""
        self.result = 0
        return self.result


if __name__ == "__main__":
    # Sample usage
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"20 / 4 = {divide(20, 4)}")

    # Calculator usage
    calc = Calculator()
    print(f"\nCalculator starting at: {calc.result}")
    print(f"After adding 10: {calc.add(10)}")
    print(f"After subtracting 3: {calc.subtract(3)}")
    print(f"After reset: {calc.reset()}")
