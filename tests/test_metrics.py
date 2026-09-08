from src.metrics import mean_absolute_error
import pytest

@pytest.fixture
def sample_observations():
    actual    = [100, 80, 120, 90]
    predicted = [90, 85, 110, 100]
    return (actual, predicted)

@pytest.fixture
def perfect_predictions():
    actual = [10, 20, 30]
    predicted = actual[:]
    return (actual, predicted)

def test_mean_absolute_error_with_valid_input(sample_observations):
    actual, predicted = sample_observations
    mae = mean_absolute_error(actual, predicted)
    assert mae == pytest.approx(8.75)

def test_mean_absolute_error_with_perfect_predictions(perfect_predictions):
    actual, predicted = perfect_predictions
    mae = mean_absolute_error(actual, predicted)
    assert mae == 0

def test_mean_absolute_error_when_actual_and_predicted_have_diff_lengths():
    actual = [10, 20, 30]
    predicted = [15, 23]
    with pytest.raises(ValueError) as exc_info:
        mean_absolute_error(actual, predicted)
    assert str(exc_info.value) == "Actual and Predicted must be of same length."

def test_mean_absolute_error_with_empty_list():
    actual, predicted = [], []
    with pytest.raises(ValueError) as exc_info:
        mean_absolute_error(actual, predicted)
    assert str(exc_info.value) == "Actual and Predicted can't be empty."

@pytest.mark.parametrize(
        "actual, predicted",
        [([10,20,30], [5,21,None]),
         ([10,20,"30"], [5,21,16])
        ]
)
def test_mean_absolute_error_with_non_numeric_types(actual, predicted):
    with pytest.raises(TypeError) as exc_info:
        mean_absolute_error(actual, predicted)
    assert str(exc_info.value) == "Input contains non-numeric value(s), this is not allowed."