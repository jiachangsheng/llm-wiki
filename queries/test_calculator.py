"""
Tests for the calculator module.
Run: pytest test_calculator.py -v
"""

import pytest
from buggy_calculator import add, subtract, multiply, divide, calculate_average, calculate_sum


class TestBasicOperations:
    def test_add(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
    
    def test_subtract(self):
        assert subtract(5, 3) == 2
        assert subtract(0, 0) == 0
    
    def test_multiply(self):
        assert multiply(3, 4) == 12
        assert multiply(0, 100) == 0
    
    def test_divide(self):
        assert divide(10, 2) == 5
        assert divide(7, 2) == 3.5
        assert divide(10, 0) == 0  # Edge case


class TestAdvancedOperations:
    def test_average_normal(self):
        """Average of [1,2,3,4,5] should be 3.0"""
        result = calculate_average([1, 2, 3, 4, 5])
        assert result == 3.0, f"Expected 3.0, got {result}"
    
    def test_average_single(self):
        """Average of [42] should be 42.0"""
        result = calculate_average([42])
        assert result == 42.0, f"Expected 42.0, got {result}"
    
    def test_sum_normal(self):
        """Sum of [10, 20, 30] should be 60"""
        result = calculate_sum([10, 20, 30])
        assert result == 60, f"Expected 60, got {result}"
    
    def test_sum_with_zero(self):
        """Sum of [0, 0, 0] should be 0"""
        result = calculate_sum([0, 0, 0])
        assert result == 0, f"Expected 0, got {result}"
