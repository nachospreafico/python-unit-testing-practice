from src.customer_summary import get_customer_summary
import pandas as pd
import numpy as np
import pytest

@pytest.fixture
def sample_orders_df():
    df = pd.DataFrame({
        "order_id": [101,102,103,104,105,106],
        "customer_id":[1,2,1,3,2,4],
        "revenue": [30.0,15.0,25.0,80.0,10.0,50.0],
    })
    return df

@pytest.fixture
def duplicated_order_id_df():
    df = pd.DataFrame({
        "order_id": [101,101,103,104,105,101],
        "customer_id":[1,2,1,3,2,4],
        "revenue": [30.0,15.0,25.0,80.0,10.0,50.0],
    })
    return df

@pytest.fixture
def na_in_order_id_df():
    df = pd.DataFrame({
        "order_id": [101,np.nan,103,104,105,106],
        "customer_id":[1,2,1,3,2,4],
        "revenue": [30.0,15.0,25.0,80.0,10.0,50.0],
    })
    return df

def test_get_customer_summary_aggregates_and_filters_customers(sample_orders_df):
    df = get_customer_summary(sample_orders_df, 50)
    expected_df = pd.DataFrame(
        {
            "customer_id": [1,3,4],
            "total_orders": [2,1,1],
            "total_revenue": [55.0,80.0,50.0]
        }
    )
    pd.testing.assert_frame_equal(df, expected_df)

def test_get_customer_summary_raises_error_for_duplicate_order_ids(duplicated_order_id_df):
    with pytest.raises(ValueError) as exc_info:
        get_customer_summary(duplicated_order_id_df, 50)
    assert str(exc_info.value) == "Duplicated values in order_id, this is not allowed."

def test_get_customer_summary_counts_orders_with_missing_order_id(na_in_order_id_df):
    total_input_rows = na_in_order_id_df.shape[0]
    df = get_customer_summary(na_in_order_id_df, 0)
    sum_of_total_orders = df["total_orders"].sum()
    assert sum_of_total_orders == total_input_rows