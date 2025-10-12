import pytest
from demo import add


def test_add_positive_integers():
    """Test adding positive integers."""
    assert add(2, 3) == 5
    assert add(10, 15) == 25
    assert add(1, 1) == 2


def test_add_negative_integers():
    """Test adding negative integers."""
    assert add(-2, -3) == -5
    assert add(-10, -15) == -25
    assert add(-1, -1) == -2


def test_add_mixed_sign_integers():
    """Test adding integers with different signs."""
    assert add(5, -3) == 2
    assert add(-5, 3) == -2
    assert add(10, -10) == 0


def test_add_floats():
    """Test adding floating point numbers."""
    assert add(2.5, 3.7) == pytest.approx(6.2)
    assert add(-1.5, -2.3) == pytest.approx(-3.8)
    assert add(1.1, -0.1) == pytest.approx(1.0)


def test_add_integer_and_float():
    """Test adding integer and float combinations."""
    assert add(5, 2.5) == 7.5
    assert add(2.5, 5) == 7.5
    assert add(-3, 1.5) == -1.5


def test_add_zeros():
    """Test adding with zeros."""
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, 5) == 5
    assert add(-3, 0) == -3


def test_add_large_numbers():
    """Test adding large numbers."""
    assert add(1000000, 2000000) == 3000000
    assert add(1.23e10, 4.56e10) == pytest.approx(5.79e10)


def test_add_small_numbers():
    """Test adding very small numbers."""
    assert add(0.0001, 0.0002) == pytest.approx(0.0003)
    assert add(-0.001, 0.001) == pytest.approx(0.0)


def test_add_commutative_property():
    """Test that addition is commutative (a + b = b + a)."""
    a, b = 7, 13
    assert add(a, b) == add(b, a)
    
    a, b = -5.5, 3.2
    assert add(a, b) == pytest.approx(add(b, a))


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (2.5, 1.5, 4.0),
    (-3.7, 2.2, -1.5),
    (100, -50, 50),
])
def test_add_parametrized(a, b, expected):
    """Parametrized test for various input combinations."""
    if isinstance(expected, float):
        assert add(a, b) == pytest.approx(expected)
    else:
        assert add(a, b) == expected


def test_add_edge_cases():
    """Test edge cases with special float values."""
    # Test with infinity
    assert add(float('inf'), 5) == float('inf')
    assert add(5, float('inf')) == float('inf')
    
    # Test with negative infinity
    assert add(float('-inf'), 5) == float('-inf')
    
    # Test NaN
    result = add(float('nan'), 5)
    assert result != result  # NaN != NaN is True


class TestAddFunction:
    """Test class for organizing related tests."""
    
    def test_return_type_consistency(self):
        """Test that return types are consistent with input types."""
        # Int + Int should return int
        result = add(2, 3)
        assert isinstance(result, int)
        
        # Float + anything should return float
        result = add(2.0, 3)
        assert isinstance(result, float)
        
        result = add(2, 3.0)
        assert isinstance(result, float)
    
    def test_precision_handling(self):
        """Test floating point precision handling."""
        result = add(0.1, 0.2)
        assert result == pytest.approx(0.3)
        
        # Test that we don't have floating point precision issues
        assert add(0.1, 0.1) == pytest.approx(0.2)


if __name__ == "__main__":
    # Run tests if script is executed directly
    pytest.main([__file__])
