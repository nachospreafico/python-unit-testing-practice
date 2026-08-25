from src.calculations import calculate_conversion_rate
import pytest

def test_scenario_1():
    assert calculate_conversion_rate(20, 100) == 0.2

def test_scenario_2():
    assert calculate_conversion_rate(0, 100) == 0.0

def test_scenario_3():
    assert calculate_conversion_rate(100, 100) == 1.0

def test_scenario_4():
    assert calculate_conversion_rate(1, 3) == pytest.approx(1/3)


@pytest.mark.parametrize("conversions, visitors", [(10, 0), (10, -5), (-1, 100), (101, 100)])
def test_value_error_scenarios(conversions, visitors):
    with pytest.raises(ValueError):
        calculate_conversion_rate(conversions, visitors)

@pytest.mark.parametrize("conversions, visitors", [(20.5, 100), (10, 99.5)])
def test_type_error_scenarios(conversions, visitors):
    with pytest.raises(TypeError):
        calculate_conversion_rate(conversions, visitors)

# def test_scenario_5():
#     with pytest.raises(ValueError):
#         calculate_conversion_rate(10, 0) # Visitors must be greater than zero

# def test_scenario_6():
#     with pytest.raises(ValueError):
#         calculate_conversion_rate(10, -5) # Visitors must be greater than zero

# def test_scenario_7():
#     with pytest.raises(ValueError):
#         calculate_conversion_rate(-1, 100) # Conversions cannot be negative

# def test_scenario_8():
#     with pytest.raises(ValueError):
#         calculate_conversion_rate(101, 100) # Conversions cannot exceed visitors

# def test_scenario_9():
#     with pytest.raises(TypeError):
#         calculate_conversion_rate(20.5, 100) # Conversions must be a non-negative integer

# def test_scenario_10():
#     with pytest.raises(TypeError):
#             calculate_conversion_rate(10, 99.5) # Visitors must be a non-negative integer        