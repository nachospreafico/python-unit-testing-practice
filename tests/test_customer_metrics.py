import pytest
import pandas as pd
import numpy as np
from src.customer_metrics import calculate_customer_metrics

@pytest.fixture
def sample_orders_df():
    df = pd.DataFrame(
        {
            "order_id": [101,102,103,104,105],
            "customer_id": [1,2,1,3,2],
            "revenue": [50.0, 20.0, 30.0, 100.0, 40.0]
        }
    )
    return df

@pytest.fixture
def expected_output():
    df = pd.DataFrame(
        {
            "customer_id": [1,2,3],
            "total_orders": [2,2,1],
            "total_revenue": [80.0, 60.0, 100.0],
            "average_order_value": [40.0, 30.0, 100.0]
        }
    )
    return df

def test_output_df_matches_expected(sample_orders_df, expected_output):
    df = calculate_customer_metrics(sample_orders_df)
    pd.testing.assert_frame_equal(df, expected_output)


def test_function_raises_value_error_with_negative_revenue():
    df = pd.DataFrame(
        {
            "order_id": [101,102,103,104,105],
            "customer_id": [1,2,1,3,2],
            "revenue": [50.0, -20.0, 30.0, 100.0, -40.0]
        }
    )
    with pytest.raises(ValueError) as exc_info:
        calculate_customer_metrics(df)
    assert str(exc_info.value) == "Negative value(s) in revenue column. This is not allowed."


def test_function_raises_value_error_when_duplicated_order_id():
    df = pd.DataFrame(
        {
            "order_id": [101,101,103,101,105],
            "customer_id": [1,2,1,3,2],
            "revenue": [50.0, 20.0, 30.0, 100.0, 40.0]
        }
    )
    with pytest.raises(ValueError) as exc_info:
        output_df = calculate_customer_metrics(df)
    assert str(exc_info.value) == "Duplicated values in order_id, this is not allowed."

def test_function_raises_value_error_when_missing_value_revenue():
    df = pd.DataFrame(
        {
            "order_id": [101,102,103,104,105],
            "customer_id": [1,2,1,3,2],
            "revenue": [50.0, np.nan, 30.0, np.nan, 40.0]
        }
    )
    with pytest.raises(ValueError) as exc_info:
        calculate_customer_metrics(df)
    assert str(exc_info.value) == "Missing value(s) in revenue, this is not allowed."

def test_function_raises_key_error_when_missing_revenue_column(sample_orders_df):
    df = sample_orders_df.drop(columns=["revenue"])
    with pytest.raises(KeyError) as exc_info:
        calculate_customer_metrics(df)
    assert str(exc_info.value.args[0]) == "Missing required column: revenue"