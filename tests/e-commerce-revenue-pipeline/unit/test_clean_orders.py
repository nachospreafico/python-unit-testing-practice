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
