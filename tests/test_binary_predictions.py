import pytest
from src.binary_predictions import evaluate_binary_predictions

@pytest.mark.parametrize(
    "y_true, y_pred, expected_error , expected_message",
    [
        ([1, 0, 1], [1, 2, 1], ValueError, "Input values must be either 1 or 0."),
        ([1.0, 0, 1], [1, 0, 1], TypeError, "Input values must be integers."),
        ([1, 0, "1"], [1, 0, 1], TypeError, "Input values must be integers."),
        ([1, 0, 1], [1, 0, True], TypeError, "Input values must be integers."),
        ((1, 0, 1), [1, 1, 1], TypeError, "Input iterables must be of type list."),
        ([1, 0, 1], (1, 1, 1), TypeError, "Input iterables must be of type list."),
        ([], [1, 1, 1], ValueError, "Input lists can't be empty."),
        ([1, 0, 1], [], ValueError, "Input lists can't be empty."),
        ([1, 0], [1, 0, 1], ValueError, "Input lists must have the same length."),
    ]
)
def test_function_raises_proper_error_with_invalid_input(y_true, y_pred, expected_error , expected_message):
    with pytest.raises(expected_error) as exc_info:
        evaluate_binary_predictions(y_true, y_pred)
    assert str(exc_info.value) == expected_message

def test_function_returns_correct_output():
    y_true = [1, 1, 0, 0]
    y_pred = [1, 0, 1, 0]
    expected_output = {
        "true_positives": 1,
        "true_negatives": 1,
        "false_positives": 1,
        "false_negatives": 1,
        "accuracy": pytest.approx(0.5)
    }
    func_output = evaluate_binary_predictions(y_true, y_pred)
    assert func_output == expected_output

def test_function_does_not_mutate_either_original_input_lists():
    original_y_true, original_y_pred = [1, 1, 0, 0], [1, 0, 1, 0]
    expected_y_true, expected_y_pred = [1, 1, 0, 0], [1, 0, 1, 0]
    evaluate_binary_predictions(original_y_true, original_y_pred)
    assert original_y_true == expected_y_true
    assert original_y_pred == expected_y_pred