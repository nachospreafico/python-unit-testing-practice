import pytest
import pandas as pd
import numpy as np
from src.ecommerce_pipeline import clean_orders

@pytest.fixture
def sample_input_df():
    return pd.DataFrame({
        "order_id": [1, 2, 3, 4, 5],
        "customer_id": [101, 101, 102, 103, 102],
        "quantity": [5, 10, 3, 5, 7],
        "unit_price": [3.00, 2.00, 4.00, 5.00, 2.00]
    })

@pytest.mark.parametrize(
    "missing_column",
    ("order_id", "customer_id", "quantity", "unit_price")
)
def test_function_raises_key_error_when_missing_required_columns(missing_column, sample_input_df):
    df = sample_input_df.copy()
    df = df.drop(columns=missing_column)
    with pytest.raises(KeyError) as exc_info:
        clean_orders(df)
    assert exc_info.value.args[0] == "Missing required column(s)"

def test_function_outputs_correct_df_when_missing_values_in_quantity_or_unit_price(sample_input_df):
    df = sample_input_df.copy()
    df["quantity"] = df["quantity"].astype(object)
    df.loc[2, "quantity"] = np.nan
    df.loc[4, "unit_price"] = np.nan
    expected_df = pd.DataFrame(
        {
            "order_id": [1, 2, 4],
            "customer_id": [101, 101, 103],
            "quantity": [5, 10, 5],
            "unit_price": [3.00, 2.00, 5.00]
        }
    )
    func_output = clean_orders(df)
    pd.testing.assert_frame_equal(func_output, expected_df)

@pytest.mark.parametrize(
    "invalid_type",
    (1.0, 1.5, "1", True)
)
def test_function_raises_proper_error_when_invalid_type_in_quantity(invalid_type, sample_input_df):
    df = sample_input_df.copy()
    df["quantity"] = df["quantity"].astype(object)
    df.loc[2, "quantity"] = invalid_type
    with pytest.raises(TypeError) as exc_info:
        clean_orders(df)
    assert str(exc_info.value) == "Invalid data type in quantity column."

@pytest.mark.parametrize(
    "invalid_value",
    (0, -1)
)
def test_function_raises_proper_error_when_invalid_value_in_quantity(invalid_value, sample_input_df):
    df = sample_input_df.copy()
    df.loc[2, "quantity"] = invalid_value
    with pytest.raises(ValueError) as exc_info:
        clean_orders(df)
    assert str(exc_info.value) == "Quantity must be greater than zero."

@pytest.mark.parametrize(
    "invalid_type",
    ("3.50", True, "free")
)
def test_function_raises_proper_error_when_invalid_type_in_unit_price(invalid_type, sample_input_df):
    df = sample_input_df.copy()
    df["unit_price"] = df["unit_price"].astype(object)
    df.loc[2, "unit_price"] = invalid_type
    with pytest.raises(TypeError) as exc_info:
        clean_orders(df)
    assert str(exc_info.value) == "Invalid data type in unit_price column."

@pytest.mark.parametrize(
    "invalid_value",
    (-1.0, -0.01, float("inf"), float("-inf"))
)
def test_function_raises_value_error_when_invalid_values_in_unit_price(invalid_value, sample_input_df):
    df = sample_input_df.copy()
    df["unit_price"] = df["unit_price"].astype(object)
    df.loc[2, "unit_price"] = invalid_value
    with pytest.raises(ValueError) as exc_info:
        clean_orders(df)
    assert str(exc_info.value) == "Invalid value in unit_price column."

@pytest.mark.parametrize(
        "invalid_values, error_message",
        (
            ([1, 2, np.nan, 4, 5], "Invalid value(s) in order_id."),
            ([1, 2, None, 4, 5], "Invalid value(s) in order_id."),
            ([1, 1, 3, 4, 5], "Duplicated value(s) in order_id. This is not allowed."),
            ([1, 1, 3, 4, np.nan], "Invalid value(s) in order_id.")
        )
)
def test_function_raises_value_error_when_invalid_value_in_order_id(invalid_values, error_message, sample_input_df):
    df = sample_input_df.copy()
    df["order_id"] = df["order_id"].astype(object)
    df["order_id"] = invalid_values
    with pytest.raises(ValueError) as exc_info:
        clean_orders(df)
    assert str(exc_info.value) == error_message