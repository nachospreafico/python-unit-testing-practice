import pandas as pd
import pytest
from src.pipeline import build_customer_report

@pytest.fixture
def sample_orders_df():
    df = pd.DataFrame(
        {
            "order_id": [101,102,103,104,105],
            "customer_id": [1,2,1,3,2],
            "quantity": [10,5,5,20,10],
            "unit_price": [5.00, 10.00, 3.00, 1.00, 4.00]
        }
    )
    return df

def test_pipeline_returns_expected_df(sample_orders_df):
    expected_df = pd.DataFrame(
            {
                "customer_id": [1,2],
                "total_orders": [2,2,],
                "total_revenue": [65.00, 90.00]
            }
        )
    pipeline_output_df = build_customer_report(sample_orders_df, 50)
    pd.testing.assert_frame_equal(pipeline_output_df, expected_df)