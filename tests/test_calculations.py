from src.calculations import calculate_conversion_rate
import pytest

def test_calculate_conversion_rate():
    assert calculate_conversion_rate(20, 100) == 0.2
    assert calculate_conversion_rate(0, 100) == 0.0
    assert calculate_conversion_rate(100, 100) == 1.0
    assert calculate_conversion_rate(1, 3) == pytest.approx(1/3)
    with pytest.raises(ValueError):
        calculate_conversion_rate(10, 0) # Visitors must be greater than zero
    with pytest.raises(ValueError):
        calculate_conversion_rate(10, -5) # Visitors must be greater than zero
    with pytest.raises(ValueError):
        calculate_conversion_rate(-1, 100) # Conversions cannot be negative
    with pytest.raises(ValueError):
        calculate_conversion_rate(101, 100) # Conversions cannot exceed visitors
    with pytest.raises(TypeError):
        calculate_conversion_rate(20.5, 100) # Conversions must be a non-negative integer
    with pytest.raises(TypeError):
            calculate_conversion_rate(10, 99.5) # Visitors must be a non-negative integer        