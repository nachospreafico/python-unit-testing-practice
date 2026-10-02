from random import randint

def evaluate_binary_predictions(y_true, y_pred):
    if type(y_true) is not list or type(y_pred) is not list:
        raise TypeError("Input iterables must be of type list.")
    
    if len(y_true) == 0 or len(y_pred) == 0:
        raise ValueError("Input lists can't be empty.")
    
    if len(y_true) != len(y_pred):
        raise ValueError("Input lists must have the same length.")

    valid_values = (0, 1)

    results = {
        "true_positives": 0,
        "true_negatives": 0,
        "false_positives": 0,
        "false_negatives": 0,
        "accuracy": 0
    }

    for i in range(len(y_true)):
        if (
            type(y_true[i]) is not int or type(y_pred[i]) is not int
        ):
            raise TypeError("Input values must be integers.")
        
        if y_true[i] not in valid_values or y_pred[i] not in valid_values:
            raise ValueError("Input values must be either 1 or 0.")

        if y_true[i] == 1 and y_pred[i] == 1: # TP case
            results["true_positives"] += 1
        elif y_true[i] == 0 and y_pred[i] == 0: # TN case
            results["true_negatives"] += 1
        elif y_true[i] == 0 and y_pred[i] == 1: # FP case
            results["false_positives"] += 1
        else: # FN case
            results["false_negatives"] += 1

    correct_predictions = results["true_positives"] + results["true_negatives"]
    all_predictions = correct_predictions + results["false_positives"] + results["false_negatives"]

    results["accuracy"] = correct_predictions / all_predictions

    return results