import pytest
import pandas as pd
from src.calculate_customer_retention import calculate_customer_retention
import numpy as np
from datetime import date, timedelta

@pytest.fixture
def sample_input_df():
    return pd.DataFrame(
        {
            "order_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
            "customer_id": [1, 2, 1, 1, 4, 2, 1, 2, 3, 1],
            "order_date": [
                "2026-03-12",
                "2026-03-12",
                "2026-04-03",
                "2026-04-10",
                "2026-08-03",
                "2026-05-12",
                "2026-06-12",
                "2026-08-04",
                "2026-08-28",
                "2026-09-12",
            ],
            "revenue": [20.0, 15.0, 0.0, 40.0, 15.0, 20.0, 25.0, 30.0, 35.0, 20.0],
        }
    )


@pytest.fixture
def sample_output_df():
    return pd.DataFrame(
        {
            "customer_id": [1, 2, 3, 4],
            "total_orders": [5, 3, 1, 1],
            "total_revenue": [105.0, 65.0, 35.0, 15.0],
            "first_order_date": [
                "2026-03-12",
                "2026-03-12",
                "2026-08-28",
                "2026-08-03",
            ],
            "last_order_date": [
                "2026-09-12",
                "2026-08-04",
                "2026-08-28",
                "2026-08-03",
            ],
            "customer_status": [
                "Active Repeat",
                "Active Repeat",
                "Active New",
                "Inactive",
            ],
        }
    )

@pytest.mark.parametrize(
    "dropped_col",
    ["order_id", "customer_id", "revenue", "order_date"]
)
def test_function_raises_key_error_when_missing_required_column(dropped_col, sample_input_df):
    df = sample_input_df.drop(columns=dropped_col)
    ref_date = "2026-10-03"
    with pytest.raises(KeyError) as exc_info:
        calculate_customer_retention(df, ref_date)
    assert exc_info.value.args[0] == "Missing required column(s)."

@pytest.mark.parametrize(
        "order_id_values, expected_error, expected_error_message",
        [
            ([101, 102, 101, 104, 105, 106, 107, 108, 109, 110], ValueError, "Duplicated value(s) in order_id. This is not allowed."),
            ([101, 102, np.nan, 104, 105, 106, 107, 108, 109, 110], ValueError, "Missing value(s) in order_id. This is not allowed."),
            ([101, 102, np.nan, 104, 101, 106, 107, 108, 109, 110], ValueError, "Missing value(s) in order_id. This is not allowed.")
        ]
)
def test_function_raises_proper_error_when_invalid_input_in_order_id(order_id_values, expected_error, expected_error_message, sample_input_df):
    df = sample_input_df.copy()
    ref_date = "2026-10-03"
    df["order_id"] = order_id_values
    with pytest.raises(expected_error) as exc_info:
        calculate_customer_retention(df, ref_date)
    assert str(exc_info.value) == expected_error_message

def test_function_raises_value_error_when_missing_customer_id(sample_input_df):
    df = sample_input_df.copy()
    ref_date = "2026-10-03"
    df.loc[7, "customer_id"] = np.nan
    with pytest.raises(ValueError) as exc_info:
        calculate_customer_retention(df, ref_date)
    assert str(exc_info.value) == "Missing value(s) in customer_id. This is not allowed."

@pytest.mark.parametrize(
    "order_date_values, expected_error, expected_error_message",
    [
        ("Not a date", ValueError, "Invalid date value(s) in order_date. This is not allowed."),
        (np.nan, ValueError, "Invalid date value(s) in order_date. This is not allowed."),
    ]
)
def test_function_raises_proper_errors_when_invalid_values_in_order_date(order_date_values, expected_error, expected_error_message, sample_input_df):
    df = sample_input_df.copy()
    ref_date = "2026-10-03"
    df.loc[7, "order_date"] = order_date_values
    with pytest.raises(expected_error) as exc_info:
        calculate_customer_retention(df, ref_date)
    assert str(exc_info.value) == expected_error_message

@pytest.mark.parametrize(
    "revenue_value, expected_error, expected_error_msg",
    [
        ("20.99", TypeError, "Invalid type(s) in revenue. This is not allowed."),
        (True, TypeError, "Invalid type(s) in revenue. This is not allowed."),
        (np.nan, ValueError, "Missing value(s) in revenue. This is not allowed."),
        (-0.01, ValueError, "Negative value(s) in revenue. This is not allowed.")
    ]
)
def test_function_raises_proper_error_when_invalid_values_in_revenue(revenue_value, expected_error, expected_error_msg, sample_input_df):
    df = sample_input_df.copy()
    ref_date = "2026-10-03"
    df["revenue"] = df["revenue"].astype(object)
    df.loc[5, "revenue"] = revenue_value
    with pytest.raises(expected_error) as exc_info:
        calculate_customer_retention(df, ref_date)
    assert str(exc_info.value) == expected_error_msg

@pytest.mark.parametrize(
    "date, expected_error, expected_error_msg",
    [
        ("not a date", ValueError, "Reference date is invalid"),
        (np.nan, ValueError, "Reference date is invalid"),
        (None, ValueError, "Reference date is invalid"),
        (date.today() + timedelta(days=1), ValueError, "Reference date is in the future")
    ]
)
def test_function_raises_proper_error_when_invalid_ref_date(date, expected_error, expected_error_msg, sample_input_df):
    df = sample_input_df.copy()
    ref_date = date
    with pytest.raises(expected_error) as exc_info:
        calculate_customer_retention(df, ref_date)
    assert str(exc_info.value) == expected_error_msg

def test_function_raises_error_when_order_date_is_later_than_reference_date(sample_input_df):
    df = sample_input_df.copy()
    ref_date = "2026-10-03"
    later_order_date = "2026-10-04"
    df.loc[5, "order_date"] = later_order_date
    with pytest.raises(ValueError) as exc_info:
        calculate_customer_retention(df, ref_date)
    assert str(exc_info.value) == "Order date cannot be later than reference date"

def test_function_returns_expected_output(sample_input_df, sample_output_df):
    df = sample_input_df.copy()
    ref_date = "2026-10-03"
    function_output = calculate_customer_retention(df, ref_date)
    expected_output = sample_output_df.copy()
    expected_output["first_order_date"] = pd.to_datetime(expected_output["first_order_date"])
    expected_output["last_order_date"] = pd.to_datetime(expected_output["last_order_date"])
    pd.testing.assert_frame_equal(function_output, expected_output)

def test_function_does_not_mutate_original_df(sample_input_df):
    df = sample_input_df.copy()
    ref_date = "2026-10-03"
    calculate_customer_retention(df, ref_date)
    pd.testing.assert_frame_equal(df, sample_input_df)