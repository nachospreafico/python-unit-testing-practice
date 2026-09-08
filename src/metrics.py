def mean_absolute_error(actual, predicted):
    if len(actual) != len(predicted):
        raise ValueError("Actual and Predicted must be of same length.")
    if len(actual) == 0 and len(predicted) == 0:
        raise ValueError("Actual and Predicted can't be empty.")
    total_absolute_error = 0
    observations = len(actual)
    for i in range(0, observations):
        if not isinstance(actual[i], (int, float)) or not isinstance(predicted[i], (int, float)):
                    raise TypeError("Input contains non-numeric value(s), this is not allowed.")
    for i in range(0, observations):
        curr_abs_error = abs(actual[i] - predicted[i])
        total_absolute_error += curr_abs_error
    mae = total_absolute_error / observations
    return mae