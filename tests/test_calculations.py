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


@pytest.mark.parametrize("conversions, visitors, exc_message", [
    (10, 0, "Visitors must be greater than zero"),
    (10, -5, "Visitors must be greater than zero"),
    (-1, 100, "Conversions cannot be negative"),
    (101, 100, "Conversions cannot exceed visitors")])
def test_value_error_scenarios(conversions, visitors, exc_message):
    with pytest.raises(ValueError) as exc_info:
        calculate_conversion_rate(conversions, visitors)
    assert str(exc_info.value) == exc_message

@pytest.mark.parametrize("conversions, visitors, exc_message", [
    (20.5, 100, "Conversions must be a non-negative integer"),
    (10, 99.5, "Visitors must be a positive integer")])
def test_type_error_scenarios(conversions, visitors, exc_message):
    with pytest.raises(TypeError) as exc_info:
        calculate_conversion_rate(conversions, visitors)
    assert str(exc_info.value) == exc_message

#def test_non_negative_conversions():
#    with pytest.raises(ValueError) as exc_info:
#        calculate_conversion_rate(-1, 100)
#    assert str(exc_info.value) == "Conversions cannot be negative"

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
