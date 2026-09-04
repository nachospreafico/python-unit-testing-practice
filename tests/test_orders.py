from src.orders import calculate_order_revenue
import pandas as pd
import numpy as np
import pytest

@pytest.fixture
def sample_orders_df():
    test_df = pd.DataFrame(
            {
                "order_id": [101, 102, 103],
                "quantity": [2, 3, 1],
                "unit_price": [10.00, 5.00, 20.00]
            }
        )
    return test_df

@pytest.fixture
def empty_sample_orders_df():
    empty_df = pd.DataFrame(
            {
                "order_id": [],
                "quantity": [],
                "unit_price": []
                }
            )
    return empty_df

def test_calculate_order_revenue(sample_orders_df):
    df = calculate_order_revenue(sample_orders_df)
    expected_df = pd.DataFrame(
        {
            "order_id": [101, 102, 103],
            "quantity": [2, 3, 1],
            "unit_price": [10.00, 5.00, 20.00],
            "revenue": [20.00, 15.00, 20.00]
        }
    )
    pd.testing.assert_frame_equal(df, expected_df)

def test_sample_orders_df_does_not_contain_revenue(sample_orders_df):
    assert "revenue" not in sample_orders_df

@pytest.mark.parametrize(
        "column_to_remove, exc_message",
        [
            ("quantity", "Missing required column: quantity"),
            ("unit_price", "Missing required column: unit_price"),
            ("order_id", "Missing required column: order_id")
        ]
        )
def test_removing_column_from_sample_orders_df(sample_orders_df, column_to_remove, exc_message):
    dropped_col_df = sample_orders_df.drop(columns=column_to_remove)
    with pytest.raises(KeyError) as exc_info:
        calculate_order_revenue(dropped_col_df)
    assert str(exc_info.value.args[0]) == exc_message

@pytest.mark.parametrize(
        "column_to_introduce_nan",
        [
            "quantity",
            "unit_price"
        ]
)
def test_nan_values_in_sample_orders_df(sample_orders_df, column_to_introduce_nan):
    # Introduce NaN on desired column at row index 1
    sample_orders_df.loc[1, column_to_introduce_nan] = np.nan
    with pytest.raises(ValueError) as exc_info:
        calculate_order_revenue(sample_orders_df)
    assert str(exc_info.value) == f"Missing one or more values on column {column_to_introduce_nan}"

def test_empty_dataframe(empty_sample_orders_df):
    df = calculate_order_revenue(empty_sample_orders_df)
    assert "revenue" in df.columns.to_list()
    assert df.shape[0] == 0
    assert df.shape[1] == 4
    assert df.iloc[:,:-1].columns.to_list() == ["order_id", "quantity", "unit_price"]