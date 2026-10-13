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